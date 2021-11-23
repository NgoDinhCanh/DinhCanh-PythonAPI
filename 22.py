import sys
import clr
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitNodes')
import Revit
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import * 
def lstFlatten(lst):
        result = []
        for i in lst:
        	for j in i :
                 result.append(j)
        return result
def getlen_CurveShortLong(allCurve):
    len_curveShort = []
    len_curveLong = []
    curveShort = []
    curveLong = []
    a = []
    b = []
    if allCurve.Count == 4 :
        if allCurve[0].Length > allCurve[1].Length:
            len_curveShort.append(round(allCurve[1].Length))
            len_curveLong.append(round(allCurve[0].Length))
            curveShort.append(allCurve[1])
            curveLong.append(allCurve[0])
        else:
            len_curveShort.append(round(allCurve[0].Length))
            len_curveLong.append(round(allCurve[1].Length))
            curveShort.append(allCurve[0])
            curveLong.append(allCurve[1])
            
    else:
        return len_curveShort.append("None")
    return lstFlatten(len_curveLong),lstFlatten(len_curveShort)
allCurve = IN[0]
len_Curve = [getlen_CurveShortLong(i) for i in allCurve ]
OUT = len_Curve