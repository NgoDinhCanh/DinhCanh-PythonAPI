import clr
import System
import math 
from System.Collections.Generic import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*

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
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
def IsParallelC(p,q):
	return p.CrossProduct( q ).IsZeroLength()
def GridsFirstEnd(lstGrids):
	keySelect =[]
	ptsGrids =[]
	for i in lstGrids:
		crv = i.Curve
		ptsGrids.append(crv.GetEndPoint(0).X)

	ptsMaxMin = [max(ptsGrids),min(ptsGrids)]

	for i in lstGrids:
		var = i.Curve
		x = var.GetEndPoint(0).X
		for j in ptsMaxMin:
			if j==x:
				keySelect.append(i)
	return keySelect
def RefArrayFromGrids(listGrids,doc):
	refArray = ReferenceArray()
	#dùng để phân tích hình học.
	opt = Options()
	opt.ComputeReferences= True#Xác định xem các tham chiếu đến các đối tượng hình học có được tính toán hay không.
	opt.IncludeNonVisibleObjects = True#Có trích xuất các đối tượng hình học phần tử ẩn không
	opt.View = doc.ActiveView#Khung nhìn được sử dụng để trích xuất hình học.
	for i in elSelect:
		crv = i.Curve
		for j in i.get_Geometry(opt):
			if isinstance(j,Line):
				grRef = j.Reference
				refArray.Append(grRef)
	return refArray
def CurveFromGrids(listGrids,doc):
	crv = []
	#dùng để phân tích hình học.
	opt = Options()
	opt.ComputeReferences= True#Xác định xem các tham chiếu đến các đối tượng hình học có được tính toán hay không.
	opt.IncludeNonVisibleObjects = True#Có trích xuất các đối tượng hình học phần tử ẩn không
	opt.View = doc.ActiveView#Khung nhìn được sử dụng để trích xuất hình học.
	for i in elSelect:
		cr = i.Curve
		crv.append(cr)
	return crv

def OffsetPoint (line,distance):
	base =XYZ.BasisZ
	sp = line.GetEndPoint(0)
	ep = line.GetEndPoint(1)
	vt = (sp+ep).CrossProduct(base).Normalize()
	pstnew = sp+distance*vt
	return vt
class SelectionFilter(ISelectionFilter):
	def __init__(self, ctgName):
		self.ctgName = ctgName
	def AllowElement(self, element):
		if element.Category.Name == self.ctgName:
			return True
		else:
			return False
	def AllowReference(ref, xyZ):
		return False

selFilter = SelectionFilter("Grids")
elSelect = uidoc.Selection.PickElementsByRectangle(selFilter,"Selects")


curveCheck =[]

vtxPlane = XYZ.BasisZ
vtxSection = XYZ.BasisY

crvGrids= CurveFromGrids(elSelect,doc)

ptsGris1 = crvGrids[0].GetEndPoint(0)
ptsGris2 = crvGrids[0].GetEndPoint(1)

vtxFromGrids = ptsGris1-ptsGris2
try:
	refGids = RefArrayFromGrids(elSelect,doc)
	pickPoint = uidoc.Selection.PickPoint("Select Point")
	direct = vtxPlane.CrossProduct(vtxFromGrids)

	line = Line.CreateBound(pickPoint,pickPoint+direct)

	TransactionManager.Instance.EnsureInTransaction(doc)
	dim = doc.Create.NewDimension(view, line, refGids)
	TransactionManager.Instance.TransactionTaskDone()
	pass
except :
	refGids = RefArrayFromGrids(elSelect,doc)
	viewDirec = view.ViewDirection
	viewOrig = view.Origin
	TransactionManager.Instance.EnsureInTransaction(doc)
	plane = Autodesk.Revit.DB.Plane.CreateByNormalAndOrigin(viewDirec,viewOrig)
	skechtplane = Autodesk.Revit.DB.SketchPlane.Create(doc,plane)
	doc.ActiveView.SketchPlane = skechtplane;
	pickPoint = uidoc.Selection.PickPoint("Select Point")
	direct = vtxPlane.CrossProduct(vtxFromGrids)

	line = Line.CreateBound(pickPoint,pickPoint+direct)

	
	dim = doc.Create.NewDimension(view, line, refGids)
	doc.Delete(skechtplane.Id)
	TransactionManager.Instance.TransactionTaskDone()
	pass


OUT = 0