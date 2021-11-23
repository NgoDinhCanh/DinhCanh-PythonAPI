import clr
import msvcrt
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*

checkRun = IN[1]
content = IN[2]
resul = str(content)
btn = TaskDialogCommonButtons.None

if checRun == True:
    TaskDialog.Show('Result',resul,btn)

else:
    resul = 'Set True to Run'

OUT = resul