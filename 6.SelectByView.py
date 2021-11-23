
import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector, Document, Category

def tolist(x):
    if hasattr(x,'__iter__'): return x
    else : return [x]

views = tolist(UnwrapElement(IN[0]))
elements = []

for view in views:
	doc=view.Document
	#Filter ExtentElem
	collector = FilteredElementCollector(doc, view.Id).ToElements().FindAll(lambda x :  x.Category != None)
	elements.append(collector)

if len(elements)>1 : OUT = elements
else: OUT = elements[0]