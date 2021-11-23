import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import TaskDialog

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB.Events import *
from Autodesk.Revit.DB import *
from math import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def _ConvertRevitCurves(xcrv):
	if  str(xcrv.GetType()) != "Autodesk.Revit.DB.PolyLine":
		rtn=xcrv.ToProtoType()	
	else:
		pt = []
		for abc in xcrv.GetCoordinates():
			pt.append(abc.ToPoint())
		rtn = PolyCurve.ByPoints(pt)
	return rtn
	
def _Mesh2PolySurface(topo):
	vp = topo.VertexPositions
	fi = topo.FaceIndices
	xr1 = xrange(len(fi) )
	ind = [(fi[i].A, fi[i].B, fi[i].C) for i in xr1]
	ptslist = [ map(vp.__getitem__, ind[i]) for i in xr1]
	
	surf=[]
	for i in ptslist:		
		surf.append(Autodesk.DesignScript.Geometry.Surface.ByPerimeterPoints(i))
	return Autodesk.DesignScript.Geometry.PolySurface.ByJoinedSurfaces(surf)
		
DOC = DocumentManager.Instance.CurrentDBDocument
DWG = UnwrapElement(IN[0])
CRV = []
CRX = []
LAY = []
CLR = []

for abc in DWG.Geometry[ Options() ]:
	for crv in abc.GetInstanceGeometry():
		try:
			lay = DOC.GetElement(crv.GraphicsStyleId).GraphicsStyleCategory.Name
			ccc = DOC.GetElement(crv.GraphicsStyleId).GraphicsStyleCategory.LineColor
			clr = [ccc.Red, ccc.Green, ccc.Blue]
			CRX.append(_ConvertRevitCurves(crv))
			CRV.append(crv)
			LAY.append(lay)
			CLR.append(clr)
		except:			
			try:
				lay="0"
				clr=[0,0,0]
				ccc=crv.ToProtoType()
				ccc=_Mesh2PolySurface(ccc)
				if ccc != None or ccc != []:
					CRX.append(ccc)
					CRV.append(crv)
					LAY.append(lay)
					CLR.append(clr)
			except: pass
	
OUT = [CRV, CRX, LAY, CLR]
# def GetSolids(cadInstance):
#     opt = Options()
#     allSolids = []
#     geoElement = cadInstance.get_Geometry(opt)
#     for geoObject in geoElement:
#         geoInstance = geoObject.GetInstanceGeometry()
#         for geoObject2 in geoInstance: 
#             if geoObject2.GetType() == Solid and geoObject2.SurfaceArea > 0 :
#                allSolids.append(geoObject2)
#     return allSolids
# def GetHatchLayerName(cadInstance,layerName):
#     allHatch = []
#     solids = GetSolids(cadInstance)
#     if solids.Count == 0:
#          return allHatch
#     for solid in solids:
#         for face in solid.Faces :
#             graphicsStyle = cadInstance.Document.GetElement(face.GraphicsStyleId)
#             if graphicsStyle == None :
#                 continue
#             styleCategory = graphicsStyle.GraphicsStyleCategory
#             if styleCategory.Name.Equals(layerName):
#                 allHatch.Add(face)
#     return allHatch

# def allCurves(planarFace):
#     allCurves = []
#     # for edgeLoops in planarFace :
#     edge_loops = planarFace.EdgeLoops
#     for edgeArray in edge_loops:
#         for edge in edgeArray:
#             allCurves.Add(edge.AsCurve())
#     return allCurves
# def getCurveShortLong(allCurve):
#     len_curveShort = []
#     len_curveLong = []
#     curveShort = []
#     curveLong = []
#     if allCurve.Count == 4 :
#         if allCurve[0].Length > allCurve[1].Length:
#             len_curveShort.append(round(allCurve[1].Length))
#             len_curveLong.append(round(allCurve[0].Length))
#             curveShort.append(allCurve[1])
#             curveLong.append(allCurve[0])
#         else:
#             len_curveShort.append(round(allCurve[0].Length))
#             len_curveLong.append(round(allCurve[1].Length))
#             curveShort.append(allCurve[0])
#             curveLong.append(allCurve[1])
#     else:
#         return len_curveShort.append("None")

#     return len_curveLong,len_curveShort,curveLong,curveShort

def verticesColumn(planarFace):
    # for i in planarFace:
    vertices = planarFace.Triangulate().Vertices
    verticesColumn = (vertices[0].Add(vertices[2]))/2 
    return verticesColumn

def Angel(curveShort):
    direc_curveShort = curveShort.GetEndPoint(1).Subtract(curveShort.GetEndPoint(0)).Normalize()
    angle = XYZ.BasisX.AngleTo(direc_curveShort)
    return angle