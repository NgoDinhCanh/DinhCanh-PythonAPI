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
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms.DataVisualization') 
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
# import ngodinhcanh as ndc 

doc = DocumentManager.Instance.CurrentDBDocument 
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument 

obType = ObjectType.Element
ref = uidoc.Selection.PickObject(obType,'Please select model Cad import')
SelectedCadLink = doc.GetElement(ref)

clr.AddReference("DSCoreNodes")
import DSCore
rtn=[]
cat=SelectedCadLink.Category.SubCategories.GetEnumerator()
while cat.MoveNext():
	rtn.append(cat.Current.Name)
	DSCore.List.Sort(rtn)

fasymbol = FilteredElementCollector(doc).OfClass(FamilySymbol).ToElements()
symbol = []
symbol1= []
for i in fasymbol:
    if i.FamilyName == "ALB_STR_Rectangular Concrete Column":
        symbol.append(i.FamilyName)
        symbol1.append(i)
# Level Name
lv = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType().ToElements()
lvs = []
for i in lv:
	lvs.append(Element.Name.__get__(i))
# def trả về Element 
def get_element(lst,string):
	for i in lst:
		if Element.Name.__get__(i)== string: return i
def get_element2(lst,string):
	for i in lst:
		if i.FamilyName == string: return i		

def GetSolids(cadInstance):
    opt = Options()
    allSolids = []
    geoElement = cadInstance.get_Geometry(opt)
    for geoObject in geoElement:
        geoInstance = geoObject.GetInstanceGeometry()
        for geoObject2 in geoInstance: 
            if geoObject2.GetType() == Solid and geoObject2.SurfaceArea > 0 :
               allSolids.append(geoObject2)
    return allSolids
# Form 
class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._btnOk = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._comboBox3)
		self._groupBox1.Controls.Add(self._comboBox2)
		self._groupBox1.Controls.Add(self._comboBox1)
		self._groupBox1.Location = System.Drawing.Point(3, 3)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(380, 110)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Input"
		# 
		# btnOk
		# 
		self._btnOk.Location = System.Drawing.Point(227, 117)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(75, 27)
		self._btnOk.TabIndex = 1
		self._btnOk.Text = "Ok"
		self._btnOk.UseVisualStyleBackColor = True
		self._btnOk.Click += self.Button1Click
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(308, 117)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(75, 27)
		self._btnCancel.TabIndex = 2
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = True
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(90, 19)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(284, 21)
		self._comboBox1.TabIndex = 0

        
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Location = System.Drawing.Point(90, 53)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(284, 21)
		self._comboBox2.TabIndex = 1
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Location = System.Drawing.Point(90, 81)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(130, 21)
		self._comboBox3.TabIndex = 2
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(9, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(74, 18)
		self._label1.TabIndex = 3
		self._label1.Text = "Layer Pile :"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(9, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(74, 18)
		self._label2.TabIndex = 4
		self._label2.Text = "Family Pile :"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(10, 84)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(74, 18)
		self._label3.TabIndex = 5
		self._label3.Text = "Level :"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLightLight
		self.ClientSize = System.Drawing.Size(394, 148)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnOk)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "ModelinCad"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)



	def BtnOkClick(self, sender, e):
		pass

	def BtnCancelClick(self, sender, e):
		pass