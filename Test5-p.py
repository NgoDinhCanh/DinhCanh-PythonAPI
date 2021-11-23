import clr
import msvcrt
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*

content = IN[1]
resul = str(IN[1])
btn = TaskDialogCommonButtons.None
TaskDialog.Show('Result',resul,btn)

OUT = resul