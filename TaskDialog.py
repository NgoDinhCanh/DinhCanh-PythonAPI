import clr 
import msvcrt
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import * 

checkRun = IN[1]
content = IN[2]

result =str(content)

btn = TaskDialogCommonButtons.None

if checkRun == True:
    TaskDialog.Show('Result',result,btn)
else:
    result = " Set True to Run " 

OUT = result