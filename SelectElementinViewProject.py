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

allElements = FilteredElementCollector(doc,view.Id).ToElement()
gettem = view.IsTemporaryHideIsolateActive()
#Code 
class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._btn = System.Windows.Forms.CheckBox()
		self._btnHide = System.Windows.Forms.Button()
		self._btnIsolate = System.Windows.Forms.Button()
		self._btnReset = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._btnSelect = System.Windows.Forms.Button()
		self._Element = System.Windows.Forms.CheckedListBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox1.Controls.Add(self._Element)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(306, 502)
		self._groupBox1.TabIndex = 1
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "All Element in Project"
		# 
		# btn
		# 
		self._btn.Location = System.Drawing.Point(12, 520)
		self._btn.Name = "btn"
		self._btn.Size = System.Drawing.Size(104, 24)
		self._btn.TabIndex = 7
		self._btn.Text = "Check All/None"
		self._btn.UseVisualStyleBackColor = True
		self._btn.CheckedChanged += self.BtnCheckedChanged
		# 
		# btnHide
		# 
		self._btnHide.Location = System.Drawing.Point(335, 345)
		self._btnHide.Name = "btnHide"
		self._btnHide.Size = System.Drawing.Size(92, 31)
		self._btnHide.TabIndex = 8
		self._btnHide.Text = "Hide"
		self._btnHide.UseVisualStyleBackColor = True
		self._btnHide.Click += self.BtnHideClick
		# 
		# btnIsolate
		# 
		self._btnIsolate.Location = System.Drawing.Point(335, 382)
		self._btnIsolate.Name = "btnIsolate"
		self._btnIsolate.Size = System.Drawing.Size(92, 31)
		self._btnIsolate.TabIndex = 9
		self._btnIsolate.Text = "Isolate"
		self._btnIsolate.UseVisualStyleBackColor = True
		self._btnIsolate.Click += self.BtnIsolateClick
		# 
		# btnReset
		# 
		self._btnReset.Location = System.Drawing.Point(335, 419)
		self._btnReset.Name = "btnReset"
		self._btnReset.Size = System.Drawing.Size(92, 31)
		self._btnReset.TabIndex = 10
		self._btnReset.Text = "Reset"
		self._btnReset.UseVisualStyleBackColor = True
		self._btnReset.Click += self.BtnResetClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(335, 456)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(92, 31)
		self._btnClose.TabIndex = 11
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# btnSelect
		# 
		self._btnSelect.Location = System.Drawing.Point(335, 308)
		self._btnSelect.Name = "btnSelect"
		self._btnSelect.Size = System.Drawing.Size(92, 31)
		self._btnSelect.TabIndex = 13
		self._btnSelect.Text = "Select"
		self._btnSelect.UseVisualStyleBackColor = True
		self._btnSelect.Click += self.BtnSelectClick
		# 
		# Element
		# 
        self._Element.DisplayMember = "Name" # Để xác định name của check list Box
		self._Element.CheckOnClick = True
		self._Element.FormattingEnabled = True
		self._Element.Location = System.Drawing.Point(7, 20)
		self._Element.Name = "Element"
		self._Element.Size = System.Drawing.Size(293, 469)
		self._Element.Sorted = True
		self._Element.TabIndex = 0
		self._Element.TabStop = False
        for i in allElements:
            self._Element.Items.Add(i)
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(439, 554)
		self.Controls.Add(self._btnSelect)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnReset)
		self.Controls.Add(self._btnIsolate)
		self.Controls.Add(self._btnHide)
		self.Controls.Add(self._btn)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Select Model Element In View"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

	def BtnSelectClick(self, sender, e):
        self.select = []
        Collection = List[ElementId]()
        for i in self._Element.CheckedItems:
            try:
                Collection.Add(i.Id)
                self.select.append(i)
            except:
                pass
        uidoc.Selection.SetElementIds(Collection)
        self.Close
		pass

	def BtnHideClick(self, sender, e):
        self.select = []
        for i in self._Element.CheckedItems:
            var = i.Id 
            self.select.append(var)
        oleId = List[ElementId](self.select)
        TransactionsManager.Instance.EnsureInTransaction(doc)
        hide = view.HideElementsTemporary(oleId)
        TransactionsManager.Instance.TransactionTaskDone()
		pass

	def BtnIsolateClick(self, sender, e):
        self.select = []
        for i in self._Element.CheckedItems:
            var = i.Id 
            self.select.append(var)
        isoId = List[ElementId](self.select)
        TransactionsManager.Instance.EnsureInTransaction(doc)
        isolate = view.HideElementsTemporary(isoId)
        TransactionsManager.Instance.TransactionTaskDone()
		pass

	def BtnResetClick(self, sender, e):
        TransactionsManager.Instance.EnsureInTransaction(doc)
        view.DisableTemporaryViewMode
        (TemporaryViewMode.TemporaryHideIsolate)
        TransactionsManager.Instance.TransactionTaskDone()
        self.Close
		pass

	def BtnCloseClick(self, sender, e):
        self.Close()
		pass

	def BtnCheckedChanged(self, sender, e):
        var = self._Element.CheckedItems.Count
        for i in range(var):
            if self._btn.Checked == True:
                self._Element.SetItemChecked(i,True)
            else:
                self._Element.SetItemChecked(i,False)
		pass
form = MainForm()
Application.Run(form)
OUT = form.select