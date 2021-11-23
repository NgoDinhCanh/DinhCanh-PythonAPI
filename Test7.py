#Copyright(c) 2018, Mohammad Nawar
#BIMhex, http://BIM-hex , mohadnawar@live.com

import sys
import clr
import System
sys.path.append(r'C:\Python24\Lib')
clr.AddReference('ProtoGeometry')
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
clr.AddReference("RevitNodes")
clr.AddReference('RevitAPI')


from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import *
from Autodesk.DesignScript.Geometry import *
from Autodesk.Revit.DB import*
import Autodesk, RevitServices
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from System.Windows.Forms import Application, Form, CheckBox, DockStyle, Panel, Label,BorderStyle
from System.Windows.Forms import ComboBox, Label, Button, AnchorStyles
from System.Drawing import Size, Rectangle, Brushes, Pens, Point, Font
from System.Drawing.Drawing2D import SmoothingMode
from System import Array
from RevitServices.Persistence import DocumentManager

global view
global selection
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
view = uidoc.ActiveView
selection = uidoc.Selection

pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
doc = DocumentManager.Instance.CurrentDBDocument
bics = System.Enum.GetValues(BuiltInCategory)
cdata = list()

for bic in bics:
	try:
		cdata.append((Revit.Elements.Category.ById(ElementId(bic).IntegerValue), Revit.Elements.Category.ById(ElementId(bic).IntegerValue).Name))
	except:
		pass

y = cdata
o1 = []
for k in y:
	o1.append(k[1])

o1= sorted(o1)

o2 = []
for i in o1:
	for j, val in enumerate(y):
		s = 1
		if i == val[1]:
			o2.append(val[0])

global o3 
o3 = []

for w in o2:
	if w not in o3:
		o3.append(w)
        
class IForm(Form):
 
    def __init__(self):

        self.Text = "Filter Form"
        self.Size = Size(600, 430)
        self.CenterToScreen()
		
        self.cb = ComboBox()
        self.cb.Parent = self
        self.cb.Width = 300 
        self.cb.Location = Point(50, 50)
        self.cb.Enabled = True
        
        font = Font("Serif", 10)
        
        self.text1 = Label()
        self.text1.Parent = self
        self.text1.Text = "Category: "
        self.text1.Location = Point(50, 20)
        self.text1.Width = 70 
        self.text1.BorderStyle = BorderStyle.FixedSingle;
        
        self.text = Label()
        self.text.Parent = self
        self.text.Font = font
        self.text.Text = "BIMhex"
        self.text.Location = Point(430, 130)
       
       
        for x in o3:	
        	self.cb.Items.Add(x.Name)   
        
        self.cb.SelectionChangeCommitted += self.OnChanged
        
        self.cb1 = CheckBox()
        self.cb1.Parent = self
        self.cb1.Location = Point(50, 100)
        self.cb1.Text = "Filter By Family Type"
        self.cb1.Width = 200
        self.cb1.Checked = False
        self.cb1.Enabled = False
        
        self.cb1.CheckedChanged += self.OnChanged1
        
        self.cb2 = ComboBox()
        self.cb2.Parent = self
        self.cb2.Width = 300 
        self.cb2.Location = Point(50, 130)
        self.cb2.Enabled = False
        self.cb2.Items.Clear()     
        #self.cb2.SelectionChangeCommitted += self.OnChanged2 
        
        self.cb3 = CheckBox()
        self.cb3.Parent = self
        self.cb3.Location = Point(50, 160)
        self.cb3.Text = "Filter By Family Name"
        self.cb3.Width = 200
        self.cb3.Checked = False
        self.cb3.Enabled = False
 
        self.cb3.CheckedChanged += self.OnChanged3 

        self.cb4 = ComboBox()
        self.cb4.Parent = self
        self.cb4.Width = 300 
        self.cb4.Location = Point(50, 190)
        self.cb4.Enabled = False
        self.cb4.Items.Clear()    

        self.cb5 = CheckBox()
        self.cb5.Parent = self
        self.cb5.Location = Point(50, 230)
        self.cb5.Text = "Isolate in the view"
        self.cb5.Width = 200
        self.cb5.Checked = False
        self.cb5.Enabled = False
        self.cb5.CheckedChanged += self.OnChanged5
		
        self.cb6 = CheckBox()
        self.cb6.Parent = self
        self.cb6.Location = Point(300, 230)
        self.cb6.Text = "Select in the view"
        self.cb6.Width = 200
        self.cb6.Checked = False
        self.cb6.Enabled = False
        self.cb6.CheckedChanged += self.OnChanged6

        self.cb7 = CheckBox()
        self.cb7.Parent = self
        self.cb7.Location = Point(50, 260)
        self.cb7.Text = "Hide in the view"
        self.cb7.Width = 200
        self.cb7.Checked = False
        self.cb7.Enabled = False
        self.cb7.CheckedChanged += self.OnChanged7

        self.cb8 = CheckBox()
        self.cb8.Parent = self
        self.cb8.Location = Point(300, 260)
        self.cb8.Text = "UnHide in the view"
        self.cb8.Width = 200
        self.cb8.Checked = False
        self.cb8.Enabled = False
        self.cb8.CheckedChanged += self.OnChanged8
        
        btn = Button()
        btn.Parent = self
        btn.Text = "Run"
        btn.Location = Point(120, 320)
        btn.Click += self.buttonPressed

        btn1 = Button()
        btn1.Parent = self
        btn1.Text = "Cancel"
        btn1.Location = Point(220, 320)
        btn1.Click += self.buttonPressed1
        
        self.Paint += self.OnPaint
        
        
    def OnPaint(self, event):
		
        g = event.Graphics
        g.SmoothingMode = SmoothingMode.AntiAlias
       	
        p1 = Point(420, 90)
        p2 = Point(440, 55)
        p3 = Point(480, 55)
        p4 = Point(500, 90)
        p5 = Point(480, 125)
        p6 = Point(440, 125)
        g.FillPolygon(Brushes.Black, Array[Point]([p1, p2, p3, p4, p5, p6]))
        g.Dispose()
        
    def OnChanged(self, sender, event):
        self.cb1.Enabled = True
        self.cb1.Checked = False
        self.cb2.Enabled = False     
        self.cb2.Items.Clear()		
        self.cb3.Enabled = True
        self.cb3.Checked = False
        self.cb5.Enabled = True
        self.cb5.Checked = False
        self.cb6.Enabled = True
        self.cb6.Checked = False
        self.cb7.Enabled = True
        self.cb7.Checked = False
        self.cb8.Enabled = True
        self.cb8.Checked = False
        
    def OnChanged1(self, sender, event):
    
        self.cb2.SelectedIndex = -1
        self.cb2.Items.Clear()
        self.cb3.Enabled = False
        self.cb3.Checked = False

        if sender.Checked:
        	global result
        	result = []
        	self.cb2.Enabled = True
	        for x in o3:	
        		if x.Name == self.cb.Text:
        			filter = ElementCategoryFilter(System.Enum.ToObject(BuiltInCategory, x.Id))
        			result.append(FilteredElementCollector(doc).WherePasses(filter).WhereElementIsElementType().ToElements())
        	for y in result:
        		for z in y:
        			self.cb2.Items.Add(Element.Name.GetValue(z))		
        if sender.Checked == False:
        	self.cb2.Enabled = False
        	self.cb3.Enabled = True
			       	
    #def OnChanged2(self, sender, event):	
        #self.cb3.Enabled = True
        #self.cb3.Checked = False
		#self.Text = ""         
		
    def OnChanged3(self, sender, event):

        self.cb1.Enabled = False
        self.cb1.Checked = False
        self.cb4.SelectedIndex = -1
        self.cb4.Items.Clear()
        
        if sender.Checked:
        	global result
        	families = []
        	result = []
        	self.cb4.Enabled = True
	        for x in o3:	
        		if x.Name == self.cb.Text:
        			filter = ElementCategoryFilter(System.Enum.ToObject(BuiltInCategory, x.Id))
        			result.append(FilteredElementCollector(doc).WherePasses(filter).WhereElementIsElementType().ToElements())
        	for y in result:
        		for z in y:
        			k = z.FamilyName
        			if k not in families:
						families.append(k)
			for w in families:
				self.cb4.Items.Add(w)				
        if sender.Checked == False:
        	self.cb1.Enabled = True
        	self.cb4.Enabled = False

    def OnChanged5(self, sender, event):

        if sender.Checked:
        	self.cb6.Enabled = False
        	self.cb6.Checked = False
        	self.cb7.Enabled = False
        	self.cb7.Checked = False
        	self.cb8.Enabled = False
        	self.cb8.Checked = False        	
        elif sender.Checked == False:
        	self.cb6.Enabled = True
        	self.cb6.Checked = False
        	self.cb7.Enabled = True
        	self.cb7.Checked = False
        	self.cb8.Enabled = True
        	self.cb8.Checked = False        	
    def OnChanged6(self, sender, event):
    
        if sender.Checked:
        	self.cb5.Enabled = False
        	self.cb5.Checked = False
        	self.cb7.Enabled = False
        	self.cb7.Checked = False
        	self.cb8.Enabled = False
        	self.cb8.Checked = False        
        elif sender.Checked == False:
        	self.cb5.Enabled = True
        	self.cb5.Checked = False
        	self.cb7.Enabled = True
        	self.cb7.Checked = False
        	self.cb8.Enabled = True
        	self.cb8.Checked = False 
    def OnChanged7(self, sender, event):
    
        if sender.Checked:
        	self.cb5.Enabled = False
        	self.cb5.Checked = False
        	self.cb6.Enabled = False
        	self.cb6.Checked = False
        	self.cb8.Enabled = False
        	self.cb8.Checked = False        
        elif sender.Checked == False:
        	self.cb5.Enabled = True
        	self.cb5.Checked = False
        	self.cb6.Enabled = True
        	self.cb6.Checked = False
        	self.cb8.Enabled = True
        	self.cb8.Checked = False 
    def OnChanged8(self, sender, event):
    
        if sender.Checked:
        	self.cb5.Enabled = False
        	self.cb5.Checked = False
        	self.cb6.Enabled = False
        	self.cb6.Checked = False
        	self.cb7.Enabled = False
        	self.cb7.Checked = False        
        elif sender.Checked == False:
        	self.cb5.Enabled = True
        	self.cb5.Checked = False
        	self.cb6.Enabled = True
        	self.cb6.Checked = False
        	self.cb7.Enabled = True
        	self.cb7.Checked = False 
        	
    def buttonPressed(self, sender, args):

        global value
        value = ""

#------------------------------------------------------------------------------
        if self.cb1.Checked:
        	global result
        	global output
        	result = []
        	output = []
	        for x in o3:	
        		if x.Name == self.cb.Text:
        			filter = ElementCategoryFilter(System.Enum.ToObject(BuiltInCategory, x.Id))
        			result.append(FilteredElementCollector(doc).WherePasses(filter).WhereElementIsElementType().ToElements())
			for y in result:
				for z in y:
					if Element.Name.GetValue(z) == self.cb2.Text:
						collector = FilteredElementCollector(doc)
						bic = System.Enum.ToObject(BuiltInCategory, z.Category.Id.IntegerValue)
						collector.OfCategory(bic)
						output = []
						for x in collector.ToElements():
							if x.GetTypeId().IntegerValue == z.Id.IntegerValue:
								output.append(x)
			#self.Close()								
        		
#------------------------------------------------------------------------------        	
        elif self.cb3.Checked:
        	global result
        	global output
        	result = []
        	output = []
        	output1 = []
	        for x in o3:	
        		if x.Name == self.cb.Text:
        			filter = ElementCategoryFilter(System.Enum.ToObject(BuiltInCategory, x.Id))
        			result.append(FilteredElementCollector(doc).WherePasses(filter).WhereElementIsElementType().ToElements())
			for y in result:
				for z in y:
					if z.FamilyName == self.cb4.Text:
						collector = FilteredElementCollector(doc)
						bic = System.Enum.ToObject(BuiltInCategory, z.Category.Id.IntegerValue)
						collector.OfCategory(bic)
						for x in collector.ToElements():
							if x.GetTypeId().IntegerValue == z.Id.IntegerValue:
								if x.Id not in output1:
									output1.append(x.Id)
									output.append(x)

#------------------------------------------------------------------------------        	
        else:
        	global output
        	global result
        	result = []
        	output = []
        	output1 = []
	        for x in o3:
        		if x.Name == self.cb.Text:
        			filter = ElementCategoryFilter(System.Enum.ToObject(BuiltInCategory, x.Id))
        			result.append(FilteredElementCollector(doc).WherePasses(filter).WhereElementIsNotElementType().ToElements())
        	for i in result:
        		for j in i:
        			output.append(j)
        if self.cb5.Checked:  		
			v = UnwrapElement(view)
			ele = UnwrapElement(output)
			ids = []
			for item in ele:
				ids.append(item.Id)
			iele = List[ElementId](ids)
			TransactionManager.Instance.EnsureInTransaction(doc)
			try:
				if not iele:
					pass
				else:
					v.IsolateElementsTemporary(iele)
			except: 
				TransactionManager.Instance.TransactionTaskDone()
        if self.cb6.Checked:
        	highlight = []
        	elements = UnwrapElement(output)
        	for e in elements:
				highlight.append(e.Id)
				Icollection = List[ElementId](highlight)
				selection.SetElementIds(Icollection)		
	
        if self.cb7.Checked:  		
			v = UnwrapElement(view)
			ele = UnwrapElement(output)
			ids = []
			for item in ele:
				ids.append(item.Id)
			iele = List[ElementId](ids)
			TransactionManager.Instance.EnsureInTransaction(doc)
			try:
				if not iele:
					pass
				else:
					v.HideElements(iele)
			except: 
				TransactionManager.Instance.TransactionTaskDone()

        if self.cb8.Checked:  		
			v = UnwrapElement(view)
			ele = UnwrapElement(output)
			ids = []
			for item in ele:
				ids.append(item.Id)
			iele = List[ElementId](ids)
			TransactionManager.Instance.EnsureInTransaction(doc)
			try:
				if not iele:
					pass
				else:
					v.UnhideElements(iele)
			except: 
				TransactionManager.Instance.TransactionTaskDone()
				
        self.Close()
        
    def buttonPressed1(self, sender, args):
        self.Close()  
if IN[0]:        
	Application.Run(IForm())
				
try:
	OUT = output
except:
	pass

