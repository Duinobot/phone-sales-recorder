from phone_inventory import *
from services.data_service import *
import sys

class InventoryApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(self,window)
        #direct singal to method of our app class
        #click buttons and inputs here
        #e.g. self.pushbutton.clicked.connect(self.method)
        
    def method:
        pass
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = FirstApp(MainWindow)
MainWindow.show()
app.exec_()