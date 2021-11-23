import sys
import clr
import math
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#Cho phép truy cập đến các node ở trong dynamo 
clr.AddReference('RevitNodes')
import Revit
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#Tham chiếu đến các element, geometry 
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
#Tham chiếu đến thư viện của Revit và Revit API
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
#Tham chiếu đến module giao diện 
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms.DataVisualization') 
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
#Lấy đối tượng document
doc = DocumentManager.Instance.CurrentDBDocument 
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument 


a = UnwrapElement(IN[1])
# def allCurves(planarFace):
def ColumnData(planarFace):
    allCurve = []
    len_curveShort = []
    verticesColumn = []
    edge_loops = planarFace.EdgeLoops
    for edgeArray in edge_loops:
        for edge in edgeArray:
            allCurve.Add(edge.AsCurve())
# # return allCurves
# def getCurveShortLong(allCurve):
#     len_curveShort = []
#     len_curveLong = []
#     curveShort = []
#     curveLong = []
    if allCurve.Count == 4 :
        if allCurve[0].Length > allCurve[1].Length:
            len_curveShort = round(allCurve[1].Length)
            len_curveLong = round(allCurve[0].Length)
            curveShort = allCurve[1]
            # curveLong = allCurve[0]
        else:
            len_curveShort = round(allCurve[0].Length)
            len_curveLong = round(allCurve[1].Length)
            curveShort = allCurve[0]
            # curveLong = allCurve[1]

        vertices = planarFace.Triangulate().Vertices
        verticesColumn = (vertices[0].Add(vertices[2]))/2

        direc_curveShort = curveShort.GetEndPoint(1).Subtract(curveShort.GetEndPoint(0)).Normalize()
        angle = XYZ.BasisX.AngleTo(direc_curveShort)
    else:
        return len_curveShort.append("None")


    return len_curveLong,len_curveShort,verticesColumn ,angle

def GetAllFamilySymbol(family):
    familySymbols = []
    # familySymbolIds = family.GetFamilySymbolIds()
    familySymbolIds = family.Ids()
    for familySymbolId in familySymbolIds :     
        symbol = family.Document.GetElement(familySymbolId) 
        familySymbols.Add(symbol)       
    return familySymbols

def GetFamilySymbolColumn(family,b,h,bPara,hPara) :
    allFamilySymbol = family.GetAllFamilySymbol()
    bParameter = allFamilySymbol[0].LookupParameter(bPara)
    hParameter = allFamilySymbol[0].LookupParameter(hPara)
    if (bParameter == None or hParameter == None) :
        return None
        # Tìm trong list type của Column đã có type với kích thước b, h chưa.
        # Nếu đã có thì lấy về type đó. chưa có thì tạo mới
    for symbol in allFamilySymbol:
        bParameter = symbol.LookupParameter(bPara)
        hParameter = symbol.LookupParameter(hPara)

        # b_value = Convert.ToDouble(bParameter.GetValue())
        # h_value = Convert.ToDouble(hParameter.GetValue())

        b_value = bParameter.AsDouble()
        h_value = hParameter.AsDouble()

        if (math.Abs(b_value - b) < 0.001 & math.Abs(h_value - h) < 0.001) :

            return symbol
        # // làm tròn đến hàng đơn vị, ví dụ: 2995.5 -> 2996
        # //double sectionX = Math.Round(DLQUnitUtils.FeetToMm(b), 0);
        # //double sectionY = Math.Round(DLQUnitUtils.FeetToMm(h), 0);
        # //string name = string.Concat(sectionX, "x", sectionY);

        newName = str.Concat((b*304.8).ToString(), 
                "x", (h*304.8).ToString())

        if (newName.Equals("0x0")): 
            return None
            # if (name.Equals("0x0") || Math.Abs(sectionX) < 0.01 ||
            #     Math.Abs(sectionY) < 0.01) return null;

        result = None
        tx = Transaction(family.Document)    
        tx.Start("Create new Column Type")
        s1 = allFamilySymbol[0].Duplicate(newName)
        s1.LookupParameter(bPara).Set(b)
        s1.LookupParameter(hPara).Set(h)
        result.Add(s1)
        tx.Commit()        
    return result

def GetValue(Pra ,asValueString):
    if Pra == None :
        return str.Empty
    if asValueString & Pra.StorageType != StorageType.String :
        return Pra.AsValueString()

c = GetFamilySymbolColumn(a,10,10,"b","h")  
OUT = c
                   



