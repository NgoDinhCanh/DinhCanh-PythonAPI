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
u = IN[1]
v = IN[2]

point_x = []
point_y = []
x_distribution1 = []
x_distribution2 = []
x_distribution3 = []
y_distribution1 = []
y_distribution2 = []
y_distribution3 = []
#---------------------- center point
center_coord = surface.CurvatureAtParameter(0.5,0.5)
center_point = center_coord.Origin
center_point_x = center_point.X
center_point_y = center_point.Y
#---------------------- max and min point
perimeter_curves = surface.PerimeterCurves()
for i in perimeter_curves:
	start_points = i.StartPoint
	point_x.append(start_points.X)
	point_y.append(start_points.Y)
	
max_point_x = max(point_x)
min_point_x = min(point_x)
max_point_y = max(point_y)
min_point_y = min(point_y)
#---------------------- x - distribution
x = center_point_x
while x < max_point_x:
	x_distribution1.append(x)
	x = x+u
	
x = center_point_x
while x > min_point_x:
	x_distribution1.append(x)
	x = x-u

x_distribution1.append(max_point_x)
x_distribution1.append(min_point_x)
x_distribution1.sort()

for j in x_distribution1:
	k = int(j)
	if k not in x_distribution2:
		x_distribution2.append(k)
		x_distribution3.append(j)
#---------------------- y - distribution
y = center_point_y
while y < max_point_y:
	y_distribution1.append(y)
	y = y+u
	
y = center_point_y
while y > min_point_y:
	y_distribution1.append(y)
	y = y-u

y_distribution1.append(max_point_y)
y_distribution1.append(min_point_y)
y_distribution1.sort()

for j in y_distribution1:
	k = int(j)
	if k not in y_distribution2:
		y_distribution2.append(k)
		y_distribution3.append(j)

OUT = surface,x_distribution3,y_distribution3
