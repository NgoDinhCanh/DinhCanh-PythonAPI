import clr
# Import DesignScript Grometry Library
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitServices") 
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

dimension = UnwrapElement(IN[0]) 

text = IN[1] 

TransactionManager.Instance.EnsureInTransaction(doc)

results = []

dimension.ValueOverride = str(text) 
dimension.Above = str(text)
dimension.Below = str(text) 
dimension.Prefix = str(text) 
dimension.Suffix = str(text) 

TransactionManager.Instance.TransactionTaskDone()

OUT = results