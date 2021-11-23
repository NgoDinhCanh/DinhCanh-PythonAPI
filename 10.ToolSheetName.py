import clr
# Import DesignScript Grometry Library
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

sheet1 = IN[0]
number1 = IN[1]
number2 = IN[2]
sheet2 = []

for i in range(len(number2)):
    for j in range(len(number1)):
        if number1[j] == number2[i]:
            sheet2.append(sheet1[j])


OUT = sheet2