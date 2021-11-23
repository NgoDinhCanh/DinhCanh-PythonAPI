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

doc = DocumentManager.Instance.CurrentDBDocument
View = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._btnBrowse = System.Windows.Forms.Button()
		self._btnOk = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(1, 4)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(424, 55)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Improt Data"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(62, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Name File :"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(64, 16)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(354, 20)
		self._textBox1.ReadOnly = True
		self._textBox1.TabIndex = 1
		self._textBox1.TabStop = False
		# 
		# btnBrowse
		# 
		self._btnBrowse.Location = System.Drawing.Point(436, 20)
		self._btnBrowse.Name = "btnBrowse"
		self._btnBrowse.Size = System.Drawing.Size(75, 23)
		self._btnBrowse.TabIndex = 1
		self._btnBrowse.Text = "Browse..."
		self._btnBrowse.UseVisualStyleBackColor = True
		self._btnBrowse.Click += self.BtnBrowseClick
		# 
		# btnOk
		# 
		self._btnOk.Location = System.Drawing.Point(350, 65)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(75, 23)
		self._btnOk.TabIndex = 2
		self._btnOk.Text = "Ok"
		self._btnOk.UseVisualStyleBackColor = True
		self._btnOk.Click += self.BtnOkClick
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(436, 65)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(75, 23)
		self._btnCancel.TabIndex = 3
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = True
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLightLight
		self.ClientSize = System.Drawing.Size(523, 90)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnOk)
		self.Controls.Add(self._btnBrowse)
		self.Controls.Add(self._groupBox1)
		self.ForeColor = System.Drawing.SystemColors.ControlText
		self.Name = "MainForm"
		self.ShowIcon = False
		self.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Import Excel"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)

		self.re = None
	def BtnOkClick(self, sender, e):
		self.fileName = self._textBox1.Text
		self.re = DialogResult.OK
		self.Close()
		pass
	def BtnCancelClick(self, sender, e):
		self.re = DialogResult.Cancel
		self.Close()
		pass
	def BtnBrowseClick(self, sender, e):
		ofd = OpenFileDialog()
		dr = ofd.ShowDialog()
		self.fileName = ofd.FileName
		if dr == DialogResult.OK:
			self._textBox1.Text = self.fileName
		
		pass
f =MainForm()
dialogResult = f.ShowDialog()
OUT = False


