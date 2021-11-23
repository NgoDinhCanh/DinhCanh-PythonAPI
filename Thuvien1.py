from Autodesk.Revit.DB import FilteredWorksetCollector, WorksetKind

# document instance
doc = __revit__.ActiveUIDocument.Document

# collect user created worksets
worksets = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()

# loop worksets
for workset in worksets:
	# print name, workset
	print workset.Name,workset