
import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
import System

name = IN[0]
options = DWGExportOptions()
if isinstance(IN[1], Autodesk.Revit.DB.ExportColorMode):
	colors=IN[1]
else:
	colors=System.Enum.Parse(Autodesk.Revit.DB.ExportColorMode, IN[1])
options.Colors = colors
if isinstance(IN[2], Autodesk.Revit.DB.ACADVersion):
	version=IN[2]
else:
	version=System.Enum.Parse(Autodesk.Revit.DB.ACADVersion, IN[2])
options.FileVersion = version
if isinstance(IN[3], Autodesk.Revit.DB.ExportUnit):
	unit=IN[3]
else:
	unit=System.Enum.Parse(Autodesk.Revit.DB.ExportUnit, IN[3])
options.TargetUnit = unit
options.SharedCoords = IN[4]
options.MergedViews = IN[5]
options.LayerMapping = ""

TransactionManager.Instance.EnsureInTransaction(doc)
result = Autodesk.Revit.DB.ExportDWGSettings.Create(doc,name,options)
TransactionManager.Instance.TransactionTaskDone()

OUT = result