from phone_inventory import *
from services.data_service import *
import sys

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