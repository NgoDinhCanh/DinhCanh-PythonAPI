import clr
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

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._btnOk = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._checkedListBox = System.Windows.Forms.CheckedListBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox1.Controls.Add(self._checkedListBox)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(548, 248)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "List Check"
		# 
		# btnOk
		# 
		self._btnOk.Location = System.Drawing.Point(404, 267)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(75, 23)
		self._btnOk.TabIndex = 0
		self._btnOk.TabStop = False
		self._btnOk.Text = "Ok"
		self._btnOk.UseVisualStyleBackColor = True
		self._btnOk.Click += self.BtnOkClick
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(485, 267)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(75, 23)
		self._btnCancel.TabIndex = 1
		self._btnCancel.Text = "Cancel"
		self._btnCancel.UseVisualStyleBackColor = True
		self._btnCancel.Click += self.BtnCancelClick
		# 
		# checkedListBox
		# 
		self._checkedListBox.FormattingEnabled = True
		self._checkedListBox.Location = System.Drawing.Point(7, 20)
		self._checkedListBox.Name = "checkedListBox"
		self._checkedListBox.Size = System.Drawing.Size(535, 199)
		self._checkedListBox.TabIndex = 0
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLightLight
		self.ClientSize = System.Drawing.Size(572, 302)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnOk)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "WPF EX"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnOkClick(self, sender, e):
		pass

	def BtnCancelClick(self, sender, e):
		pass
f =MainForm()
dialogResult = f.ShowDialog()

