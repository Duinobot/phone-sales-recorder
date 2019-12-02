from phone_inventory import *
from services.data_service import *
import sys
from mongoengine import *
from Data.attribute import *

#connect database with pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client.learning_mongo
#connect database with mongoengine
connect('learning_mongo')

try:
	add_phone(imei="657657",model="iPhone 7",storage="128GB",color="Silver",grade="A")
except:
	pass

class InventoryApp(Ui_MainWindow):
	def __init__(self, window):
		self.setupUi(window)
		#direct singal to method of our app class
		#click buttons and inputs here
		#e.g. self.pushbutton.clicked.connect(self.method)
		#self.addPhone_model_comboBox.
		self.addPhone_addPhone_pushButton.clicked.connect(self.addPhone_AddButtonClicked)
		self.display_updated_phones_in_table()


	def addPhone_AddButtonClicked(self):
		model = self.addPhone_model_comboBox.currentText()
		storage = self.addPhone_storage_comboBox.currentText()
		color = self.addPhone_color_comboBox.currentText()
		grade = self.addPhone_grade_comboBox.currentText()
		imei = self.addPhone_imei_lineEdit.text()
		full_name = model + " " + storage + "GB [" + grade + " Grade] [" + color +"]"
		if addPhone_productID_lineEdit.text() == None:
			product_id = Phone.objects.filter(Q(full_name=full_name)&Q(product_id__exists=True)).first().product_id
		else:
			product_id = self.addPhone_productID_lineEdit.text()

		if (model == "" or storage == "" or grade == "" or color == "" or imei == ""):
			self.addPhone_displayFullName_label.setText("Please select all attributes and enter IMEI")
		else:
			self.display_fullname_and_imei(full_name=full_name,imei=imei)
			if search_by_imei(imei).count() != 0:
				self.addPhone_displayIMEI_label.setText("IMEI Already Exists")
			else:
				newPhone = add_phone(imei=imei, model=model, storage=storage, color=color, grade=grade, product_id=product_id)
				self.display_updated_phones_in_table()
			#display new phone in table below


	def display_fullname_and_imei(self,full_name,imei):
		self.addPhone_displayFullName_label.setText(full_name)
		self.addPhone_displayIMEI_label.setText(imei)		

	def display_updated_phones_in_table(self):
		self.addPhone_newQty_tableWidget.setRowCount(0)
  		#get change_checked is fales
		name_list = Phone.objects(Q(change_checked=False) & Q(customer_id__exists=False)).distinct(field="full_name")
		#display all unchecked phone (id,full_name,qty,confirm button) in table
		#id change
		self.addPhone_newQty_tableWidget.cellChanged.connect(self.update_phone_id)
		for name in name_list:
			row = name_list.index(name)
			self.addPhone_newQty_tableWidget.insertRow(row)
			self.addPhone_newQty_tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(Phone.objects(full_name=name)[0].product_id)))
			self.addPhone_newQty_tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(name)))
			self.addPhone_newQty_tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(Phone.objects(full_name=name).count())))
			self.ok_btn = QtWidgets.QPushButton("OK~")
			self.addPhone_newQty_tableWidget.setCellWidget(row,3,self.ok_btn)
			self.ok_btn.clicked.connect(self.ok_btn_clicked)
			#ok_btn			
		#display confirm buttons

	def update_phone_id(self):
		id = self.addPhone_newQty_tableWidget.currentItem()
		if id != None:
			if id.column()==0:
				full_name = self.addPhone_newQty_tableWidget.item(id.row(),1).text()
				Phone.objects(full_name=full_name).update(product_id=id.text())
	
	def ok_btn_clicked(self):
		ok_btn = QtWidgets.QApplication.focusWidget()
		index = self.addPhone_newQty_tableWidget.indexAt(ok_btn.pos())
		if index.isValid():
			print(index.row(),index.column())
			#set change_check status to True
			full_name = self.addPhone_newQty_tableWidget.item(index.row(),1).text()
			Phone.objects(full_name=full_name).update(change_checked=True)
			self.display_updated_phones_in_table()



	


	 

	
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = InventoryApp(MainWindow)
MainWindow.show()
app.exec_()