import sys
import clr
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitNodes')
import Revit
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import * 

doc = DocumentManager.Instance.CurrentDBDocument 
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument 

FamilyInstance = NewFamilyInstance(TamCot,familySymbol,BaseLevel, StructuralType)
FamilyInstance.get_Parameter(BuiltInParameter.FAMILY_BASE_LEVEL_PARAM).SetValue(BaseLevel.Id)
FamilyInstance.get_Parameter(BuiltInParameter.FAMILY_TOP_LEVEL_PARAM).Set(TopLevel.Id)
FamilyInstance.get_Parameter(BuiltInParameter.FAMILY_BASE_LEVEL_OFFSET_PARAM).Set(BaseOffset)
FamilyInstance.get_Parameter(BuiltInParameter.FAMILY_TOP_LEVEL_OFFSET_PARAM).Set(TopOffset)

# axis = Line.CreateUnbound(columnData.TamCot, XYZ.BasisZ)
# ElementTransformUtils.RotateElement(_viewModel.Doc,instance.Id, axis,columnData.GocXoay)

# newColumns.Add(instance.Id);