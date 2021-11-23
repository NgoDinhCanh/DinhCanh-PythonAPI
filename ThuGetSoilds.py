import sys
import clr
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#Cho phép truy cập đến các node ở trong dynamo 
clr.AddReference('RevitNodes')
import Revit
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#Tham chiếu đến các element, geometry 
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
#Tham chiếu đến thư viện của Revit và Revit API
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
#Tham chiếu đến module giao diện 
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms.DataVisualization') 
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
# import ngodinhcanh as ndc 
#Lấy đối tượng document
doc = DocumentManager.Instance.CurrentDBDocument 
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument 

################################################################
def get_element(lst,string):
	for i in lst:
		if Element.Name.__get__(i)== string: return i
def get_element2(lst,string):
	for i in lst:
		if i.FamilyName == string: return i	

def duplicateFamilyType(lstFamilyType,lstDuplicateName):
    result =[]
    for i in lstDuplicateName:
        try:
            TransactionManager.Instance.EnsureTransaction(doc)
            newsymbol = [j.Duplicate(s) for j in lstFamilyType]
            result.Add(j.ToDSType(True) for j in newsymbol)
            TransactionManager.Instance.TransactionTaskDone()
        except: "None"
        return result
# try:
#     dupFaType = duplicateFamilyType(familyType,duplicateName)[0]
#     OUT = [i.Family for i in dupFaType] [0]
# except: 
#     OUT = [i.Family for i in familyType]
def getCurveShortLong(allCurve):
    len_curveShort = []
    len_curveLong = []
    curveShort = []
    curveLong = []
    if allCurve.Count == 4 :
        if allCurve[0].Length > allCurve[1].Length:
            len_curveShort.append(round(allCurve[1].Length))
            len_curveLong.append(round(allCurve[0].Length))
            curveShort.append(allCurve[1])
            curveLong.append(allCurve[0])
        else:
            len_curveShort.append(round(allCurve[0].Length))
            len_curveLong.append(round(allCurve[1].Length))
            curveShort.append(allCurve[0])
            curveLong.append(allCurve[1])
    else:
        return len_curveShort.append("None")

    return len_curveLong,len_curveShort,curveLong,curveShort

def GetSolids(cadInstance):
    opt = Options()
    allSolids = []
    geoElement = cadInstance.get_Geometry(opt)
    for geoObject in geoElement:
        geoInstance = geoObject.GetInstanceGeometry()
        for geoObject2 in geoInstance: 
            if geoObject2.GetType() == Solid and geoObject2.SurfaceArea > 0 :
               allSolids.append(geoObject2)
    return allSolids
def Dict(lst):
    s = []
    for i in lst:
       if i not in s:
          s.append(i)
    return s
def GetAllLayer(cadInstance):
    opt = Options()
    allLayer = []
    geoElement = cadInstance.get_Geometry(opt)
    for geoObject in geoElement:
        geoInstance = geoObject.GetInstanceGeometry()
        for geoObject2 in geoInstance: 
            if geoObject2.GetType() == Solid : 
                if geoObject2.SurfaceArea > 0 :
                   faceArray = geoObject2.Faces
                   for face in faceArray:
                       elementId = face.GraphicsStyleId
                       graphicsStyle = cadInstance.Document.GetElement(elementId)
                       styleCategory = graphicsStyle.GraphicsStyleCategory
                       allLayer.Add(styleCategory.Name)

            else:
                elementId = geoObject2.GraphicsStyleId
                graphicsStyle = cadInstance.Document.GetElement(elementId)
                styleCategory = graphicsStyle.GraphicsStyleCategory
                allLayer.Add(styleCategory.Name)
    allLayers = Dict(allLayer)
    allLayers.sort()
    return allLayers
def GetHatchLayerName(cadInstance,layerName):
    allHatch = []
    solids = GetSolids(cadInstance)
    if solids.Count == 0:
         return allHatch
    for solid in solids:
        for face in solid.Faces :
            graphicsStyle = cadInstance.Document.GetElement(face.GraphicsStyleId)
            if graphicsStyle == None :
                continue
            styleCategory = graphicsStyle.GraphicsStyleCategory
            if styleCategory.Name.Equals(layerName):
                allHatch.Add(face)
    return allHatch
def allCurves(planarFace):
    allCurves = []
    for edgeLoops in planarFace :
        edge_loops = edgeLoops.EdgeLoops
        for edgeArray in edge_loops:
            for edge in edgeArray:
                allCurves.Add(edge.AsCurve())
    return allCurves
def verticesColumn(planarFace):
    # for i in planarFace:
    vertices = planarFace.Triangulate().Vertices
    verticesColumn = (vertices[0].Add(vertices[2]))/2 
    return verticesColumn
def Angel(curveShort):
    direc_curveShort = curveShort.GetEndPoint(1).Subtract(curveShort.GetEndPoint(0)).Normalize()
    angle = XYZ.BasisX.AngleTo(direc_curveShort)
    return angle


layerName = IN[1][0]
SelectedCadLink = UnwrapElement(IN[1][6])
allSolid = GetSolids(SelectedCadLink)
allHatchs = GetHatchLayerName(SelectedCadLink,layerName)   
allCurve = allCurves(allHatchs)
# len_ShortLong = [getCurveShortLong(i) for i in allCurve]
vertice_Column = [verticesColumn(i) for i in allHatchs]
# angel = [Angel(i) for i in (len_ShortLong[3][3])]
# OUT = allSolid,allHatchs,allCurve,len_ShortLong,vertice_Column,angel
OUT = allSolid,allHatchs,allCurve,vertice_Column