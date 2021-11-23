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
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._comboBox1)
		self._groupBox1.Location = System.Drawing.Point(6, -1)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(380, 53)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Input"
		# 
		# btnOk
		# 
		self._btnOk.Location = System.Drawing.Point(233, 58)
		self._btnOk.Name = "btnOk"
		self._btnOk.Size = System.Drawing.Size(75, 27)
		self._btnOk.TabIndex = 1
		self._btnOk.Text = "Ok"
		self._btnOk.UseVisualStyleBackColor = True
		self._btnOk.Click += self.BtnOkClick
		# 
		# btnCancel
		# 
		self._btnCancel.Location = System.Drawing.Point(311, 58)
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
		# label1
		# 
		self._label1.Location = System.Drawing.Point(9, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(74, 18)
		self._label1.TabIndex = 3
		self._label1.Text = "Layer Grids :"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLightLight
		self.ClientSize = System.Drawing.Size(394, 90)
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