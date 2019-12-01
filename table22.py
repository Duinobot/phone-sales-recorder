# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table 22.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#connect database with mongoengine

class Ui_MainWindow(object):
	def loadData(self):
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(4)
		#id_chage
		self.tableWidget.cellChanged.connect(self.change_id)
		for row in range(0,6):
			self.tableWidget.insertRow(row)
			row_id = "row_id:" + str(row) 
			self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(row_id)))
			self.confirm_btn = QtWidgets.QPushButton("Confirm")
			self.tableWidget.setCellWidget(row,3,self.confirm_btn)
			self.confirm_btn.clicked.connect(self.confirm_btn_clicked)
			for column in range(1,3):
				self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem(str(row*4+column)))
					
	#id_change
	def change_id(self):
		id = self.tableWidget.currentItem()
		if id != None:
			print("id:{} added to database".format(id.text()))

	def confirm_btn_clicked(self):
		button = QtWidgets.QApplication.focusWidget()
		index = self.tableWidget.indexAt(button.pos())
		if index.isValid(): 
			print(index.row(),index.column())

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(300, 110, 311, 261))
		self.tableWidget.setRowCount(3)
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setObjectName("tableWidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(410, 400, 75, 23))
		self.pushButton.setObjectName("pushButton")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.pushButton.clicked.connect(self.loadData)

		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "load"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
