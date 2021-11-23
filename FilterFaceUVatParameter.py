import sys
import clr
#Cho Phép truy cập đến các đối tượng, view, sheet, element.... trong view hiện hành và chỉnh sửa được nó:
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#Cho phép truy cập đến các node ở trong dynamo mà liên quan tới Revit:
clr.AddReference('RevitNodes')
import Revit
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#Tham chiếu đến các element, geometry trong dynamo:
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
#Tham chiếu đến thư viện của Revit và Revit API
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
#Tham chiếu đến module giao diện người dùng (thư viện đồ họa)
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms.DataVisualization') #Trực quan hóa dữ liệu. Biểu thị dữ liệu dưới dạng chart,đồ thị..
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
#Lấy đối tượng document
doc = DocumentManager.Instance.CurrentDBDocument #Đại diện cho 1 dự án đang được mở (view hiện hành)
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument #Có thể truy cập các data từ RevitAPI

# Select model elements
select_ref = uidoc.Selection.PickObject(ObjectType.Element,'Please select model element') #Mới lấy ra được list tham chiếu
el = doc.GetElement(select_ref) #Lấy ra Family theo điểm tham chiếu ref
el_id = el.Id #Lấy ra Id của family
#GeometryInstance-->Solid-->Face
#Step 1: Retrieve geometry from element (family)
def GetGeometry(elem):
    Geo = []
    Geo_option = Options() #Phân tích tính toán, nhiều lựa chọn cho hình học
    Geo_option.ComputeReferences = True
    Geo_option.DetailLevel = ViewDetailLevel.Fine
    elemGeometry = elem.get_Geometry(Geo_option) #Lấy về hình học
    Geo.append(elemGeometry)
    return elemGeometry #Kết thúc việc thực thi hàm và gửi giá trị lại nơi mà hàm được gọi. Khi tạo hàm thì luôn
    #phải có return để có thể trả về kết quả của hàm. Nếu không mặc định là None.
    #Khi gặp từ khóa return thì hàm đó sẽ kết thúc và trả lại giá trị sau từ khóa return. 
    #Các câu lệnh sau dòng return này sẽ không có ý nghĩa. 

#Step 2: Get Solid from geometry of step 1
def GetSolid(Geo):
    Sol =[]
    for i in Geo:
        #Lấy ra tất cả các đối tượng thuộc geometry (solid, line, arc..Những đối tượng nào tạo nên geometry)
        symbol = i.GetSymbolGeometry() 
        for k in symbol:
            if k.GetType() == Solid and k.Volume >0:
                Sol.append(k)
    return Sol

#Step 3: Get Face from Solid of step 2
def GetPlanar(Sol):
    Surfa = []
    for i in Sol:
        #Lấy ra thuộc tính Face. Để ta có thể truy xuất các mặt phẳng ở trong thuộc tính Face này
        Surfa.append(i.Faces)
    return Surfa

#Các biến được đặt:
Geo = GetGeometry(el) #Gán parameter "el" cho hàm def Geometry để triết xuất ra được hình học của element đó
Sol = GetSolid(Geo) #Gán parameter "Geo" cho hàm def GetSolid để triết xuất ra được khối solid
Surfa = GetPlanar(Sol) #Gán parameter "Sol" cho hàm GetPlanar để triết xuất ra các mặt phẳng planarface

#Convert Revit to Dynamo: Get surface
get_face = [k.ToProtoType() for i in Surfa for k in i]

#Sau khi convert về surface thì ta nhận thấy cấp list quá cao. Nên ta có thể Flatten nó theo hàm sau
def flatten(x):
    result = []
    for el in x:
        #Hàm hasattr(object, attribute): Trả về true nếu thuộc tính đó thuộc đối tượng
        #Hàm isinstance(object, type): Trả về true nếu đối tượng đó có đúng kiểu type như mình kiểm tra
        #basestring: string and unicode (là các chuỗi kí tự)
        #iter: lặp qua từng phần tử  
        if hasattr(el, "__iter__") and not isinstance(el, basestring): #Có thể dùng cái này hoặc cái dưới cũng được
            #Mục địch là kiểm tra xem đối tượng el có thuộc tính __iter__ hay không. Phương thức __iter__ trả về chính đối tượng
            #của lớp đó.Là đối tượng này có thể lặp lại hay không. Có phải là 1 list hay không
            result.extend(flatten(el))
            #extend nó lặp đi lặp lại thông qua đối tượng lắp lại (iterable) và sau đó nối từng mục của 1 danh sách nào đó vào
        else:
            result.append(el)
    return result
#Xử lí ngoại lệ: Nếu try nó xử lí cái hàm def flatten(x) bị lỗi thì nó sẽ bỏ qua và xử lí hàm except.
try:
	result = flatten(get_face)
except:
	result = get_face

def flatten1(x):
    result1 = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring): 
            result1.extend(flatten1(el))
        else:
            result1.append(el)
    return result1
try:
	result1 = flatten1(Surfa)
except:
	result1 = Surfa

surface = result
u = 0.5
v = 0.5

point_x = []
point_y = []
x_distribution1 = []
x_distribution2 = []
x_distribution3 = []
y_distribution1 = []
y_distribution2 = []
y_distribution3 = []
#---------------------- center point
center_coord = surface.CurvatureAtParameter(0.5,0.5)
center_point = center_coord.Origin
center_point_x = center_point.X
center_point_y = center_point.Y
#---------------------- max and min point
perimeter_curves = surface.PerimeterCurves()
for i in perimeter_curves:
	start_points = i.StartPoint
	point_x.append(start_points.X)
	point_y.append(start_points.Y)
	
max_point_x = max(point_x)
min_point_x = min(point_x)
max_point_y = max(point_y)
min_point_y = min(point_y)
#---------------------- x - distribution
x = center_point_x
while x < max_point_x:
	x_distribution1.append(x)
	x = x+u
	
x = center_point_x
while x > min_point_x:
	x_distribution1.append(x)
	x = x-u

x_distribution1.append(max_point_x)
x_distribution1.append(min_point_x)
x_distribution1.sort()

for j in x_distribution1:
	k = int(j)
	if k not in x_distribution2:
		x_distribution2.append(k)
		x_distribution3.append(j)
#---------------------- y - distribution
y = center_point_y
while y < max_point_y:
	y_distribution1.append(y)
	y = y+u
	
y = center_point_y
while y > min_point_y:
	y_distribution1.append(y)
	y = y-u

y_distribution1.append(max_point_y)
y_distribution1.append(min_point_y)
y_distribution1.sort()

for j in y_distribution1:
	k = int(j)
	if k not in y_distribution2:
		y_distribution2.append(k)
		y_distribution3.append(j)

OUT = surface,x_distribution3,y_distribution3,result1,el_id