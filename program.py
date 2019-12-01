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
		self.addPhone_addPhone_pushButton.clicked.connect(self.display_fullname_and__imei)
		
	def addPhone_AddButtonClicked(self):
		model = self.addPhone_model_comboBox.currentText()
		storage = self.addPhone_storage_comboBox.currentText()
		color = self.addPhone_color_comboBox.currentText()
		grade = self.addPhone_grade_comboBox.currentText()
		imei = self.addPhone_imei_lineEdit.text()
		product_id = self.addPhone_productID_lineEdit.text()
		full_name = model + " " + storage + "GB [" + grade + " Grade] [" + color +"]"
		if (model == "" or storage == "" or grade == "" or color == "" or imei == ""):
			self.addPhone_displayFullName_label.setText("Please select all attributes and enter IMEI")
		else:
			self.display_fullname_and__imei(full_name=full_name,imei=imei)
			if search_by_imei(imei) == None:
				newPhone = add_phone(imei=imei, model=model, storage=storage, color=color, grade=grade, product_id=product_id)
			else:
				self.addPhone_displayIMEI_label.setText("IMEI Already Exists")
			#display new phone in table below
			
					
	def display_fullname_and__imei(full_name,imei):
		self.addPhone_displayFullName_label.setText(full_name)
		self.addPhone_displayIMEI_label.setText(imei)		

	def display_updated_phones_in_table():
		pass
		#1 Search this imei and see if already exists



	 

	
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = InventoryApp(MainWindow)
MainWindow.show()
app.exec_()