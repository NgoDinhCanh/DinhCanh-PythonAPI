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
# import ngodinhcanh as ndc 
doc = DocumentManager.Instance.CurrentDBDocument 
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument 

def duplicateFamilyType(fa,b,h,b_para,h_para):
    newName = []
    bPara = []
    hPara = []
    for i,j in zip(b,h):
        bPara.append(i)
        hPara.append(j)
        newName.append((str(i)).replace(".0","")+" "+ "x" + " "+ (str(j)).replace(".0","")+"mm")
    def lstFlatten(lst):
        result = []
        for i in lst:
            for j in i :
                result.append(j)
        return result
    family = lstFlatten(fa)          
    TransactionManager.Instance.EnsureInTransaction(doc)
    familyType = []
    for name,i,j in zip(newName,bPara,hPara):
        try:
            a = family[0].Duplicate(name)
            a.LookupParameter(b_para).Set(i)
            a.LookupParameter(h_para).Set(j)
            familyType.append(a)   
        except:
            "None"
        
    TransactionManager.Instance.TransactionTaskDone()
    return 
family = IN[0]
b = IN[1]
h = IN[2]
b_para = IN[3]
h_para = IN[4]
familyTypes = duplicateFamilyType(family,b,h,b_para,h_para)
OUT = familyTypes