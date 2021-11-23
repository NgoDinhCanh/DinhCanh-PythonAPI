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

# # Select model elements
# select_ref = uidoc.Selection.PickObjects(ObjectType.Element,'Please select model element') #Mới lấy ra được list tham chiếu
# result = []
# for i in select_ref:
#     get_el = doc.GetElement(i) #Lấy element và id
#     get_Geo = get_el.get_Geometry(Options()) 
    
#     # get_sol = SpatialElementGeometryResults.GetGeometry() #Lấy solid
#     result.append(get_Geo)

# Select model elements
#select_ref = uidoc.Selection.PickObject(ObjectType.Element,'Please select model element') #Mới lấy ra được list tham chiếu
#result = []

ref = uidoc.Selection.PickObjects(ObjectType.Element,'Please select model element')
el = []
for i in ref:
    element = doc.GetElement(i.ElementId)
    el.append(element.ToDSType(True))
    
def GetSolidElement(element):
    geo = []
    opt = Options() # Phan tic tinh toan hinh hoc 
    opt.ComputeReferences = True
    opt.IncludeNonVisibleObjects = True
    opt.DetailLevel = ViewDetailLevel.Fine
    geometry = element.get_Geometry(opt)
    for i in geometry: 
        geo.append(i)
    return geometry
def GetSolidFromGeo(lstGeo):
    sol = []
    for i in lstGeo:
        if i.GetType() == Solid and i.Volume > 0:
            sol.append(i)
        elif i.GetType() == GeometryInstance:
            var = i.GetInstanceGeometry
            for j in var:
                if j.GetType() == Solid and j.Volume > 0:
                    sol.append(j)
    return sol
def GetPlanarFromSolid(solids):
    re = []
    for i in solids:
        re.append(i.Faces)
        return re[0]
    
geo = GetSolidElement(el)
solid = GetSolidFromGeo(geo)
planar = GetPlanarFromSolid(solid)
#Output:
OUT = el