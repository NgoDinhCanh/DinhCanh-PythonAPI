import sys
import clr
#Cho Phép truy cập đến các đối tượng, view, sheet, element.... trong view hiện hành và chỉnh sửa được nó:
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#Cho phép truy cập đến các node ở trong dynamo mà liên quan tới Revit:
clr.AddReference('RevitNodes')
import Revit
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#Tham chiếu đến các element, geometry trong dynamo:
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
#Tham chiếu đến thư viện của Revit và Revit API
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
#Tham chiếu đến module giao diện người dùng (thư viện đồ họa)
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms.DataVisualization') #Trực quan hóa dữ liệu. Biểu thị dữ liệu dưới dạng chart,đồ thị..
import System.Windows.Forms
import System.Drawing
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *
#Lấy đối tượng document
doc = DocumentManager.Instance.CurrentDBDocument #Đại diện cho 1 dự án đang được mở (view hiện hành)
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument #Có thể truy cập các data từ RevitAPI

ele_Lvs = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType().ToElements()
ele_Floor = FilteredElementCollector(doc).OfClass(Floor).WhereElementIsNotElementType().ToElements()
ele_Wall = FilteredElementCollector(doc).OfClass(Wall).WhereElementIsNotElementType().ToElements()
ele_Wall = FilteredElementCollector(doc).OfClass(Grid).WhereElementIsNotElementType().ToElements()

Filter = ["Of Class" ,"Of Category"]

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btnOk = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._checkedListBox = System.Windows.Forms.CheckedListBox()
		self._label1 = System.Windows.Forms.Label()
		self._btnCheckAll = System.Windows.Forms.Button()
		self._btnCheckNone = System.Windows.Forms.Button()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self.SuspendLayout()
		# 
		# btnOk
		# 
		self._btnOk.Location = System.Drawing.Point(379, 126)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(75, 33)
		self._btnOk.TabIndex = 0
		self._btnOk.Text = "Ok"
		self._btnOk.UseVisualStyleBackColor = True
		self._btnOk.Click += self.BtnOkClick
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(460, 126)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(75, 33)
		self._btnCancel.TabIndex = 1
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = True
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(56, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(317, 21)
		self._comboBox1.TabIndex = 2
		self._comboBox1.Items.AddRange(System.Array[System.Object](Filter))
		# 
		# checkedListBox
		# 
		self._checkedListBox.FormattingEnabled = True
		self._checkedListBox.Location = System.Drawing.Point(12, 39)
		self._checkedListBox.Name = "checkedListBox"
		self._checkedListBox.Size = System.Drawing.Size(361, 94)
		self._checkedListBox.TabIndex = 3
		self._checkedListBox.SelectedIndexChanged += self.CheckedListBoxSelectedIndexChanged
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(38, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "Filter:"
		# 
		# btnCheckAll
		# 
		self._btnCheckAll.Location = System.Drawing.Point(400, 39)
		self._btnCheckAll.Name = "btnCheckAll"
		self._btnCheckAll.Size = System.Drawing.Size(114, 23)
		self._btnCheckAll.TabIndex = 6
		self._btnCheckAll.Text = "Check All"
		self._btnCheckAll.UseVisualStyleBackColor = True
		self._btnCheckAll.Click += self.BtnCheckAllClick
		# 
		# btnCheckNone
		# 
		self._btnCheckNone.Location = System.Drawing.Point(400, 68)
		self._btnCheckNone.Name = "btnCheckNone"
		self._btnCheckNone.Size = System.Drawing.Size(114, 23)
		self._btnCheckNone.TabIndex = 7
		self._btnCheckNone.Text = "Check None"
		self._btnCheckNone.UseVisualStyleBackColor = True
		self._btnCheckNone.Click += self.BtnCheckNoneClick
		# 
		# progressBar1
		# 
		self._progressBar1.Location = System.Drawing.Point(12, 136)
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(361, 23)
		self._progressBar1.TabIndex = 8
		self._progressBar1.Click += self.ProgressBar1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(542, 163)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._btnCheckNone)
		self.Controls.Add(self._btnCheckAll)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._checkedListBox)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnOk)
		self.Name = "MainForm"
		self.Text = "FilterElementCategory"
		self.ResumeLayout(False)


	def CheckedListBoxSelectedIndexChanged(self, sender, e):
		pass

	def BtnOkClick(self, sender, e):
		pass

	def BtnCancelClick(self, sender, e):
		pass

	def BtnCheckAllClick(self, sender, e):
		pass

	def BtnCheckNoneClick(self, sender, e):
		pass

	def ProgressBar1Click(self, sender, e):
		pass
form = MainForm()
Application.Run(form)
OUT = ele_Floor