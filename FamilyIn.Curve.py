
import clr
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

families = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
curveList=[]

opt = Options()
#opt.IncludeNonVisibleObjects = True
#opt.View = doc.ActiveView
#opt.ComputeReferences = True
opt.DetailLevel = ViewDetailLevel.Fine

for fam in families:
	geoEle=fam.GetOriginalGeometry(opt)
	lines=[]
	for geoInstance in geoEle:
		if isinstance(geoInstance, Curve):
			transformCurve=geoInstance.CreateTransformed(fam.GetTransform())
			#Instead of importing : clr.ImportExtensions(Revit.GeometryConversion)
			lines.append(Revit.GeometryConversion.RevitToProtoCurve.ToProtoType(transformCurve, True))
		else:
			if isinstance(geoInstance, Solid) and geoInstance.Volume == 0:
				edges=[]
				edgesArray=geoInstance.Edges
				for edge in edgesArray :
					transformCurve=edge.AsCurve().CreateTransformed(fam.GetTransform())
					edges.append(Revit.GeometryConversion.RevitToProtoCurve.ToProtoType(transformCurve, True))
				curveList.append(edges)
	curveList.append(lines)
	
OUT = filter(None,curveList)