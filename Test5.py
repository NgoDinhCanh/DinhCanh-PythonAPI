# Xóa Filter in Project
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
filters = FilteredElementCollector(doc).OfClass(ParameterFilterElement).ToElements()
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._CheckListFilter = System.Windows.Forms.CheckedListBox()
		self._CheckAll = System.Windows.Forms.CheckBox()
		self._OK = System.Windows.Forms.Button()
		self._Cancel = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._CheckAll)
		self._groupBox1.Controls.Add(self._CheckListFilter)
		self._groupBox1.Location = System.Drawing.Point(12, 11)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(503, 227)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "All Filter in Project"
		# 
		# CheckListFilter
		# 
		self._CheckListFilter.DisplayMember = 'Name' # Để xác định name của check list Box
		self._CheckListFilter.CheckOnClick = True
		self._CheckListFilter.FormattingEnabled = True
		self._CheckListFilter.Location = System.Drawing.Point(6, 22)
		self._CheckListFilter.Name = "CheckListFilter"
		self._CheckListFilter.Size = System.Drawing.Size(491, 169)
		self._CheckListFilter.Sorted = True
		self._CheckListFilter.TabIndex = 0
		self._CheckListFilter.TabStop = False
		for i in filters:
			self._CheckListFilter.Items.Add(i)
		# 
		# CheckAll
		# 
		self._CheckAll.Location = System.Drawing.Point(6, 197)
		self._CheckAll.Name = "CheckAll"
		self._CheckAll.Size = System.Drawing.Size(104, 24)
		self._CheckAll.TabIndex = 1
		self._CheckAll.Text = "Select All/None"
		self._CheckAll.UseVisualStyleBackColor = True
		self._CheckAll.CheckedChanged += self.CheckAllCheckedChanged
		# 
		# OK
		# 
		self._OK.Location = System.Drawing.Point(354, 258)
		self._OK.Name = "OK"
		self._OK.Size = System.Drawing.Size(75, 23)
		self._OK.TabIndex = 1
		self._OK.Text = "OK"
		self._OK.UseVisualStyleBackColor = True
		self._OK.Click += self.OKClick
		# 
		# Cancel
		# 
		self._Cancel.Location = System.Drawing.Point(440, 258)
		self._Cancel.Name = "Cancel"
		self._Cancel.Size = System.Drawing.Size(75, 23)
		self._Cancel.TabIndex = 2
		self._Cancel.Text = "Cancel"
		self._Cancel.UseVisualStyleBackColor = True
		self._Cancel.Click += self.CancelClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLightLight
		self.ClientSize = System.Drawing.Size(527, 290)
		self.Controls.Add(self._Cancel)
		self.Controls.Add(self._OK)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.ShowIcon = False
		self.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Delete Filter"
		self.TopMost = True
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def OKClick(self, sender, e):
		Selected =[]
		for i in self._CheckListFilter.CheckedItems:
			Selected.append(i)
		self.st = str(Selected.Count) + " Đã xóa Filter in ProJect"
		self.cnt = Selected.Count
		TransactionManager.Instance.EnsureInTransaction(doc) # Báo cáo cho Revit biết sắp sửa có 1 cái thay đổi (or giao dịch)
		for i in Selected:
			idd = i.Id
			doc.Delete(i.Id)

		TransactionManager.Instance.TransactionTaskDone() # Báo cáo cho Revit biết đã thực hiện sửa xong  (or giao dịch xong )
		self.Close()
		pass

	def CancelClick(self, sender, e):

		self.Close()
		pass
#Cần int để action phải xử lý 
	def CheckAllCheckedChanged(self, sender, e):

		#Xử lý 
		var = self._CheckListFilter.Items.Count 
		rgn = range(var)

		#for i in self._CheckListFilter.Items:
		for i in rgn:
			if self._CheckAll.Checked == True:
				self._CheckListFilter.SetItemChecked(i,True)
			else :
				self._CheckListFilter.SetItemChecked(i,False)
		pass
form = MainForm()
Application.Run(form)
OUT = form.st,form.cnt