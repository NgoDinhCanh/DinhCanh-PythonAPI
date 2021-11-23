import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
# Import geometry conversion extension methods
clr.ImportExtensions(Revit.GeometryConversion)
# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import *
# Import RevitAPI
clr.AddReference("RevitAPI")  
import Autodesk
from Autodesk.Revit.DB import * 
clr.AddReference("DSCoreNodes")
import DSCore


_path =  r'C:\Users\mohad\AppData\Roaming\Dynamo\Dynamo Revit\2.3\packages\Bimhex\bin'

import sys
sys.path.append(_path)
clr.AddReference('ProgressBar')
from AdnRme import ProgressForm

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

surface = IN[0]

#---------------------- center point
center_point = []
for i in surface:
	center_coord = i.CurvatureAtParameter(0.5,0.5) 
	center_point.append(center_coord.Origin)

OUT = center_point