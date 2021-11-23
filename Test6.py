#NgoDinhCanh
import clr 
import System 

from System.Collections.Generic import * 

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import*

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import * 

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*

clr.AddReference('RevitNodes')
import Revit 
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

def Dis

pickbox = uidoc.Selection.PickBox(Autodesk.Revit.UI.Selection.PickBoxStyle.Directional,"Hãy chọn vùng Crop View- Ngo Dinh Canh")

ptsMax = pickbox.Max
ptsMin = pickbox.Min 

ptsCheckMax = ptsMax.ToPoint()
ptsCheckMin = ptsMin.ToPoint()
cropShape = view.GetCropRegionShapeManager()

OUT = ptsMax,ptsMin,ptsCheckMax,ptsCheckMin
