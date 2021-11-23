
# Import Element wrapper extension methods
import clr
# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

import System
from System.Collections.Generic import *

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

#ProcessParallelLists borrowed from Konrad K Sobon
def ProcessList(_func, _list):
    return map( lambda x: ProcessList(_func, x) if type(x)==list else _func(x), _list )

def ProcessParallelLists(_func, *lists):
	return map( lambda *xs: ProcessParallelLists(_func, *xs) if all(type(x) is list for x in xs) else _func(*xs), *lists )

def Unwrap(item):
	return UnwrapElement(item)
# IN[0] DirectoryPath
folderPath = IN[0]
#IN[1] view
if isinstance(IN[1], list):
	views = ProcessList(Unwrap, IN[1])
else:
	views = [Unwrap(IN[1])]
# IN[2] Filename
if isinstance(IN[2], list):
	names = IN[2]
else:
	names = [IN[2]]
# IN[3] boolen
RunIt = IN[3]

def ExportDxf(name, view, folder = folderPath):
	options = DXFExportOptions()
	views = List[ElementId]()
	views.Add(view.Id)
	result = doc.Export(folder, name, views, options)
	return result

if RunIt:
	try:
		errorReport = None
		# run export
		ProcessParallelLists(ExportDxf, names, views)
		
	except:
		# if error accurs anywhere in the process catch it
		import traceback
		errorReport = traceback.format_exc()
else:
	errorReport = "Please set the RunIt to True!"

#Assign your output to the OUT variable
if errorReport == None:
	OUT = "Success"
else:
	OUT = errorReport