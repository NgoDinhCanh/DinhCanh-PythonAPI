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

fasymbol = FilteredElementCollector(doc).OfClass(FamilySymbol).OfCategory(BuiltInCategory.OST_StructuralColumns).ToElements()
symbol = []

for i in fasymbol:
	symbol.append(i.FamilyName)
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

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._comboBox4 = System.Windows.Forms.ComboBox()
		self._progressWindow = System.Windows.Forms.ProgressBar()
		self._btnOk = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._comboBox4)
		self._groupBox1.Controls.Add(self._comboBox3)
		self._groupBox1.Controls.Add(self._comboBox2)
		self._groupBox1.Controls.Add(self._comboBox1)
		self._groupBox1.Location = System.Drawing.Point(12, 1)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(508, 194)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Input Data"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox2.Controls.Add(self._btnCancel)
		self._groupBox2.Controls.Add(self._btnOk)
		self._groupBox2.Controls.Add(self._progressWindow)
		self._groupBox2.Location = System.Drawing.Point(12, 201)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(508, 56)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		# 
		# comboBox1
		# 
		self._comboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(94, 19)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(400, 21)
		self._comboBox1.TabIndex = 0
		self._comboBox1.Items.AddRange(System.Array[System.Object](rtn))	
		# 
		# comboBox2
		# 
		self._comboBox2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Location = System.Drawing.Point(94, 62)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(400, 21)
		self._comboBox2.TabIndex = 1
		self._comboBox2.Items.AddRange(System.Array[System.Object](symbol))	
		# 
		# comboBox3
		#
		self._comboBox3.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Location = System.Drawing.Point(94, 112)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(134, 21)
		self._comboBox3.TabIndex = 6
		self._comboBox3.Items.AddRange(System.Array[System.Object](lvs))	
		# 
		# comboBox4
		#
		self._comboBox4.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList 
		self._comboBox4.FormattingEnabled = True
		self._comboBox4.Location = System.Drawing.Point(94, 154)
		self._comboBox4.Name = "comboBox4"
		self._comboBox4.Size = System.Drawing.Size(134, 21)
		self._comboBox4.TabIndex = 7
		self._comboBox4.Items.AddRange(System.Array[System.Object](lvs))
		# 
		# progressWindow
		# 
		self._progressWindow.ForeColor = System.Drawing.Color.Cyan
		self._progressWindow.Location = System.Drawing.Point(7, 20)
		self._progressWindow.Name = "progressWindow"
		self._progressWindow.Size = System.Drawing.Size(284, 23)
		self._progressWindow.Style = System.Windows.Forms.ProgressBarStyle.Marquee
		self._progressWindow.TabIndex = 0
		# 
		# btnOk
		# 
		self._btnOk.Location = System.Drawing.Point(328, 13)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(84, 33)
		self._btnOk.TabIndex = 1
		self._btnOk.Text = "OK"
		self._btnOk.UseVisualStyleBackColor = True
		self._btnOk.Click += self.BtnOkClick
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(418, 13)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(84, 33)
		self._btnCancel.TabIndex = 2
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = True
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(82, 21)
		self._label1.TabIndex = 12
		self._label1.Text = "Layer of Hatch "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(6, 61)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(73, 21)
		self._label2.TabIndex = 13
		self._label2.Text = "Family"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 110)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(63, 21)
		self._label3.TabIndex = 14
		self._label3.Text = "Base Level "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(6, 154)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(64, 21)
		self._label4.TabIndex = 15
		self._label4.Text = "Top Level"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(265, 111)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(75, 21)
		self._label5.TabIndex = 16
		self._label5.Text = "Base Offset"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(265, 154)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(75, 21)
		self._label6.TabIndex = 17
		self._label6.Text = "Top Offset"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(360, 113)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(134, 20)
		self._textBox1.TabIndex = 18
		self._textBox1.Text = "0"

		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(360, 154)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(134, 20)
		self._textBox2.TabIndex = 19
		self._textBox2.Text = "0"

		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLightLight
		self.ClientSize = System.Drawing.Size(532, 261)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "ModelCadInProjectWinForm"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)
		self.btn_Ele = []
		self.allFamilies_Ele = []
		self.lvs_Ele1 = []
		self.lvs_Ele2 = []
		self.tx_Ele1 = []
		self.tx_Ele2 = []
    

	def BtnOkClick(self, sender, e):
		var1 = self._comboBox1.Text
		var2 = self._comboBox2.Text
		var3 = self._comboBox3.Text
		var4 = self._comboBox4.Text
		var5 = self._textBox1.Text
		var6 = self._textBox2.Text
		self.btn_Ele = var1
		self.allFamilies_Ele = get_element2(fasymbol,var2)
		self.lvs_Ele1 = get_element(lv,var3)
		self.lvs_Ele2 = get_element(lv,var4)
		self.tx_Ele1 = float(var5)
		self.tx_Ele2 = float(var6)
		self.Close()
        pass

	def BtnCancelClick(self, sender, e):
		self.Close()
		pass
f = MainForm()
Application.Run(f)
# allHatchs = ndc.GetHatchLayerName(SelectedCadLink,f.btn_Ele)   
# allCurve = ndc.allCurves(allHatchs)
# len_ShortLong = [ndc.getCurveShortLong(i) for i in allCurve]
# vertice_Column = [ndc.verticesColumn(i) for i in allHatchs]
# familySymbol = ndc.GetFamilySymbolColumn(f.allFamilies_Ele,len_ShortLong[1],len_ShortLong[2],"b","h")
# t = Transaction(doc,"Create Columns")
# t.Start()
# angel = [ndc.Angel(i) for i in (len_ShortLong[3][3])]
OUT = f.btn_Ele,f.allFamilies_Ele,f.lvs_Ele1,f.lvs_Ele2,f.tx_Ele1,f.tx_Ele2,SelectedCadLink
