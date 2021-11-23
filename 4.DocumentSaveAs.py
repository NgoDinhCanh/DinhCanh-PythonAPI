import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

path = IN[0]
compact = IN[1]
newcentral = IN[2]
isworkshared = IN[3]
worksetConfiguration = IN[4]
if isinstance(worksetConfiguration , basestring):
	exec("openWorksets = SimpleWorksetConfiguration.%s" % worksetConfiguration)
else:
	openWorksets = worksetConfiguration
inputdoc = IN[5] if isinstance(IN[5],list) else [IN[5]]

#Inputdoc : Part of script by Andreas Dieckmann
if inputdoc[0] == None:
    doc = DocumentManager.Instance.CurrentDBDocument
elif inputdoc[0].GetType().ToString() == "Autodesk.Revit.DB.Document":
    doc = inputdoc[0]
else: doc = DocumentManager.Instance.CurrentDBDocument

TransactionManager.Instance.ForceCloseTransaction()
if doc.IsFamilyDocument:
	path += '.rfa'
else:
	path += '.rvt'
opt = SaveAsOptions()
opt.OverwriteExistingFile = True
opt.Compact = compact
if isworkshared and newcentral:
	wsopt = WorksharingSaveAsOptions()
	#Set workset configuration
	if worksetConfiguration :
		wsopt.OpenWorksetsDefault = openWorksets
	else : wsopt.OpenWorksetsDefault = SimpleWorksetConfiguration.AskUserToSpecify
	wsopt.ClearTransmitted = True
	wsopt.SaveAsCentral = True
	opt.SetWorksharingOptions(wsopt)
try:
	doc.SaveAs(path, opt)
	OUT = True,doc
except:
	try:
		wsopt.ClearTransmitted = False
		opt.SetWorksharingOptions(wsopt)
		doc.SaveAs(path, opt)
		OUT = True,doc
	except:
		OUT = False,doc