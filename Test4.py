import clr
import System
from System.Collections.Generic import*

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView

nameLevel =[]
lvs = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType().ToElements()
#C1 for i in lvs:
   # var = i.ToDSType(True)
    #nameLevel.append(var.Name)
#C2 for i in lvs:
    #var = Element.Name.__get__(i)
   # nameLevel.append(var)
nameLevel = [Element.Name.__get__(x) for x in lvs]
# lọc 
fTypeFliter = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFoundation).WhereElementIsElementType().ToElements()
f1TypeFliter = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralFoundation).WhereElementIsNotElementType().ToElements()
f2TypeFliter = FilteredElementCollector(doc.view.Id).OfCategory(BuiltInCategory.OST_StructuralFoundation).WhereElementIsNotElementType().ToElements()
OUT = f2TypeFliter
