
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, ParameterFilterElement, SelectionFilterElement
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
name = IN[0]
view = UnwrapElement(IN[1])

elements, user_selection = [], []
# Get all ParameterFilterElements in doc
filter_elements = FilteredElementCollector(doc).OfClass(ParameterFilterElement)
filter_names = [f.Name for f in filter_elements]
filters = [f.GetElementFilter() for f in filter_elements]
filter_dict = dict(zip(filter_names, filters))

if name in filter_dict:
	filter = filter_dict[name]
	elements = FilteredElementCollector(doc,view.Id).WhereElementIsNotElementType().WherePasses(filter).ToElements()

selection_sets = FilteredElementCollector(doc,view.Id).OfClass(SelectionFilterElement)

for s in selection_sets:
	if s.Name == name:
		ids = s.GetElementIds()
		elements = [doc.GetElement(e) for e in ids]
		
OUT = elements