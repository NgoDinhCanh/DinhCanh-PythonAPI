#NgoDinhCanh
import clr
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import unicodedata

import System
from System.Collections.Generic import*

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import*

clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Windows.Forms.DataVisualization')

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import *

clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=11.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel
from System.Runtime.InteropServices import Marshal

doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

fileName = IN[1]

ex = Excel.ApplicationClass()

ex.Visible = True

ex.DisplayAlerts = False

workbook = ex.Workbooks.Open(fileName)

ws = workbook.Worksheets.Count

value = []
for i in range(ws):
	var = workbook.Worksheets[i+1].Name
	value.append(var)

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._btnOk = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._comboBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(12, -1)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(401, 78)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Check List"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(42, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Name :"
		# 
		# comboBox1
		#
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Location = System.Drawing.Point(54, 26)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(321, 21)
		self._comboBox1.TabIndex = 1
		self._comboBox1.Items.AddRange(System.Array[System.Object](value))
		self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		
		# 
		# btnOk
		# 
		self._btnOk.Location = System.Drawing.Point(419, 12)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(75, 28)
		self._btnOk.TabIndex = 1
		self._btnOk.Text = "Ok"
		self._btnOk.UseVisualStyleBackColor = True
		self._btnOk.Click += self.BtnOkClick
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(419, 46)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(75, 28)
		self._btnCancel.TabIndex = 2
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = True
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLightLight
		self.ClientSize = System.Drawing.Size(498, 88)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnOk)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.ShowIcon = False
		self.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "List"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		
		
	def ComboBox1SelectedIndexChanged(self, sender, e):
		pass

	def BtnOkClick(self, sender, e):
		self.out = self._comboBox1.Text
		self.outIndex = self._comboBox1.SelectedIndex
		self.Close()
		pass

	def BtnCancelClick(self, sender, e):
		self.out = "Khong thuc hien"
		self.Close()
		pass
f =MainForm()
dialogResult = f.ShowDialog()

id = f.outIndex
ws = workbook.Worksheets[(index+1)]

#Cell 
x = ws.Range["A1","A30"]
y = ws.Range["B1","B30"]
z = ws.Range["C1","C30"]

x1 = x.Value2
y1 = y.Value2
z1 = z.Value2
ex.ActiveWorkbook.Close(True)
ex.Quit()

OUT = x1 , y1 , z1