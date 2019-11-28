from phone_inventory import *
from services.data_service import *
import sys
from mongoengine import *

#connect database with pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client.learning_mongo
#connect database with mongoengine
connect('learning_mongo')

add_phone(imei="657657",model="iPhone 7",storage="128GB",color="Silver",grade="A")

class InventoryApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        #direct singal to method of our app class
        #click buttons and inputs here
        #e.g. self.pushbutton.clicked.connect(self.method)
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = InventoryApp(MainWindow)
MainWindow.show()
app.exec_()