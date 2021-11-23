import clr
import System

from System.Collections.Generic import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc= DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

def Distance(p,plane):

	q = p - plane.Origin
	return plane.Normal.DotProduct(q)

def ProjectOntoPlane(pts,plane):
	d = Distance(pts,plane)
	p = pts - d*plane.Normal
	return p
	
def CurveLoopByPoint(point):
	count = point.Count
	curve = []
	crvLoop = CurveLoop()
	for i in range(0,count):
		if i != count-1:			
			crvLoop.Append(Line.CreateBound(point[i],point[i+1]))
		else:
			crvLoop.Append(Line.CreateBound(point[count-1],point[0]))
	return crvLoop

sel = Autodesk.Revit.UI.Selection
pickBox = uidoc.Selection.PickBox(sel.PickBoxStyle.Directional,"Hãy chọn vùng Crop View - Ngo Dinh Canh")

ptsList = []

ptsMax = pickBox.Max
ptsMin = pickBox.Min

#ptsCheckMax = ptsMax.ToPoint()
#ptsCheckMin = ptsMin.ToPoint()

cropShape =view.GetCropRegionShapeManager()

vextorOfView = view.UpDirection

plane = Autodesk.Revit.DB.Plane.CreateByNormalAndOrigin(vextorOfView,ptsMax)
xyz1 = ProjectOntoPlane(ptsMin,plane)
#xyz1Check = xyz1.ToPoint()

plane = Autodesk.Revit.DB.Plane.CreateByNormalAndOrigin(vextorOfView,ptsMin)
xyz2 = ProjectOntoPlane(ptsMax,plane)
#xyz2Check = xyz2.ToPoint()
ptsList.append(ptsMin)
ptsList.append(xyz1)
ptsList.append(ptsMax)
ptsList.append(xyz2)

#curve =[
    #Line.CreateBound(ptsMin,xyz1),
    #Line.CreateBound(xyz1,ptsMax),
    #Line.CreateBound(ptsMax,xyz2),
    #Line.CreateBound(xyz2,ptsMin)
 #]
#curveCheck = []
curveloop = CurveLoopByPoint(ptsList)
#for i in curveloop: curveCheck.append(i.ToProtoType())
#curveloop = CurveLoop.Create(curve)

try:
	TransactionManager.Instance.EnsureInTransaction(doc)
	view.CropBoxActive = True
	view.CropBoxVisible = True
	cropShape.SetCropShape(curveloop)
	TransactionManager.Instance.TransactionTaskDone()
	OUT = curveloop
	pass
except:
	button = TaskDialogCommonButtons.None

	TaskDialog.Show('Result',"None in View 3D",button)
	OUT = False
	pass


