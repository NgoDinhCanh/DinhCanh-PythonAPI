
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

def tolist(obj1):
    if hasattr(obj1,"__iter__"): return obj1
    else: return [obj1]

view = tolist(UnwrapElement(IN[0]))[0]
lines = tolist(IN[1])
references= IN[2]
dimensionType=tolist(UnwrapElement(IN[3]))[0]

elementsRef = ReferenceArray()
for reference in references :
	elementsRef.Append(reference)
	
TransactionManager.Instance.EnsureInTransaction(doc)
for line in lines:
	if doc.IsFamilyDocument == True :
		if IN[3]== None: 
			dim = doc.FamilyCreate.NewDimension(view, line.ToRevitType(), elementsRef).ToDSType(True)
		else:
			dim = doc.FamilyCreate.NewDimension(view, line.ToRevitType(), elementsRef,dimensionType).ToDSType(True)
	else:
		if IN[3]== None: 
			dim = doc.Create.NewDimension(view, line.ToRevitType(), elementsRef).ToDSType(True)
		else:
			dim = doc.Create.NewDimension(view, line.ToRevitType(), elementsRef,dimensionType).ToDSType(True)
TransactionManager.Instance.TransactionTaskDone()

OUT=dim