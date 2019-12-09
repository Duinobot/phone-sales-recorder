from ui import *
from services.data_service import *
import sys
from Data.attribute import *
import datetime

class InventoryApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        #direct singal to method of our app class
        #click buttons and inputs here	
        #e.g. self.pushbutton.clicked.connect(self.method)
        #self.addPhone_model_comboBox.
        self.addPhone_addPhone_pushButton.clicked.connect(self.addPhone_AddButtonClicked)
        self.addPhone_imei_lineEdit.returnPressed.connect(self.addPhone_AddButtonClicked)
        self.display_updated_phones_in_summary_table()
        #store customer_id for addCustomer Tab use
        self.customer_id = None
        #customer selected on PhoneOut customer
        self.customer_selected = None
        #phone list on PhoneOut Imei Table
        self.phone_list = None
        self.reset_diplay_customer_combobox()
        self.addCustomer_addCustomer_pushCustomer.clicked.connect(self.add_customer_btn_clicked)
        self.addCustomer_editSearch_pushButton.clicked.connect(self.edit_customer_search_clicked)
        self.addCustomer_editConfirm_pushButton.clicked.connect(self.edit_customer_confirm_clicked)
        self.phoneOut_findCustomer_comboBox.activated.connect(self.display_selected_customer)
        self.phoneOut_addCustomer_pushButton.clicked.connect(self.go_to_add_customter_tab)
        self.phoneOut_findIMEI_lineEdit.returnPressed.connect(self.phoneOut_imei_find_display)
        self.phoneOut_findIMEI_pushButton.clicked.connect(self.phoneOut_imei_find_display)
        self.phoneOut_assignPhoneToCustomer_pushButton.clicked.connect(self.assign_phone_to_customer)
        #initiate phone attribute box
        try:
            self.initiate_phone_attribute_box()
        except:
            pass
        self.display_new_phones_in_newPhone_table()
        self.addPhone_pushButton_confirmChange.clicked.connect(self.confirmChange_button_clicked)

    def confirmChange_button_clicked(self):
        for phone in self.new_phone_list:
            phone.input_confirmed = True
            phone.save()
        self.display_new_phones_in_newPhone_table()

    def initiate_phone_attribute_box(self):
        self.addPhone_storage_comboBox.addItem("")
        self.addPhone_color_comboBox.addItem("")
        self.addPhone_grade_comboBox.addItem("")
        self.addPhone_model_comboBox.addItem("")
        self.addPhone_storage_comboBox.addItems(get_attribute_list(name="storage"))
        self.addPhone_color_comboBox.addItems(get_attribute_list(name="color"))
        self.addPhone_grade_comboBox.addItems(get_attribute_list(name="grade"))
        self.addPhone_model_comboBox.addItems(get_attribute_list(name="model"))
 
    def reset_diplay_customer_combobox(self):
                #set combobox customer name values
        self.customer_list = Customer.objects
        #initiate auto completer for combox
        self.display_items = [] 
        for customer in self.customer_list:
            dispaly_item = customer.company+"/"+customer.name
            self.phoneOut_findCustomer_comboBox.addItem(dispaly_item)
            self.display_items.append(dispaly_item)
        self.completer = QtWidgets.QCompleter(self.display_items)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.phoneOut_findCustomer_comboBox.setCompleter(self.completer)

    def assign_phone_to_customer(self):
        if self.customer_selected is None:
            QtWidgets.QMessageBox.critical(self.tab_2,"Error","Please select customer")
            return
        try:
            imei_selected_rows = sorted(set(index.row() for index in self.phoneOut_findIMEI_tableWidget.selectedIndexes()))
        except:
            QtWidgets.QMessageBox.critical(self.tab_2,"Error","imei not selected")
            return
        for row in imei_selected_rows:
            #assign add customer_id to this phone
            try:
                phone_selected = self.phone_list[row]
            except:
                pass
            phone_selected.customer_id = self.customer_selected.id
            phone_selected.date_out = datetime.datetime.now()
            phone_selected.date_modified = datetime.datetime.now()
            phone_selected.save()
            self.phoneOut_imei_find_display()

    def phoneOut_imei_find_display(self):
        imei = self.phoneOut_findIMEI_lineEdit.text()
        if self.phoneOut_checkBox_includeSold.checkState() == 0:
            self.phone_list = list(Phone.objects.filter(Q(imei__iendswith = imei) & Q(customer_id__exists=False)))
        else:
            self.phone_list = list(Phone.objects.filter(imei__iendswith = imei))
        self.display_imei_found_phoneOut()

    def display_imei_found_phoneOut(self):
        self.phoneOut_findIMEI_tableWidget.setRowCount(0)
        if self.phoneOut_checkBox_includeSold.checkState() == 0:
            for phone in self.phone_list:
                row = self.phone_list.index(phone)
                self.phoneOut_findIMEI_tableWidget.insertRow(row)
                self.phoneOut_findIMEI_tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(phone.imei)))
                self.phoneOut_findIMEI_tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(phone.full_name)))
        else:
            for phone in self.phone_list:
                row = self.phone_list.index(phone)
                self.phoneOut_findIMEI_tableWidget.insertRow(row)
                self.phoneOut_findIMEI_tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(phone.imei)))
                self.phoneOut_findIMEI_tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(phone.full_name)))
                try:
                    customer = Customer.objects.get(id=phone.customer_id)
                    
                    self.phoneOut_findIMEI_tableWidget.setColumnCount(4)
                    self.phoneOut_findIMEI_tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(phone.date_modified)))
                    self.phoneOut_findIMEI_tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(customer.company)))
                    #set header items
                except:
                    pass

    def go_to_add_customter_tab(self):
        self.tabWindow.setCurrentWidget(self.tab_3)

    def display_selected_customer(self):
        try:
              currentIndex = self.display_items.index(self.phoneOut_findCustomer_comboBox.currentText())
        except:
            return
        self.customer_selected = self.customer_list[currentIndex]
        self.phoneOut_displayCustomer_tableWidget.setRowCount(1)
        self.phoneOut_displayCustomer_tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(str(self.customer_selected.name)))
        self.phoneOut_displayCustomer_tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem(str(self.customer_selected.company)))

    def edit_customer_confirm_clicked(self):
        try:
              customer = Customer.objects.get(id=self.customer_id)
        except:
            QtWidgets.QMessageBox.critical(self.tab_3,"Error","no such customer")
            return
        customer.company = self.addCustomer_editCompany_lineEdit.text()
        customer.name = self.addCustomer_editName_lineEdit.text()
        customer.mobile = self.addCustomer_editPhone_lineEdit.text()
        customer.email = self.addCustomer_editEmail_lineEdit.text()
        customer.save()
        QtWidgets.QMessageBox.about(self.tab_3,"Success","Customer information updated")
        self.reset_diplay_customer_combobox()

    def edit_customer_search_clicked(self):
        company = self.addCustomer_editCompany_lineEdit.text()
        name = self.addCustomer_editName_lineEdit.text()
        mobile = self.addCustomer_editPhone_lineEdit.text()
        email = self.addCustomer_editEmail_lineEdit.text()
        if company != "":
            customer = Customer.objects.filter(company__icontains=company).first()
            try:
                self.display_customer_info_for_edit(customer)
            except:
                return
        elif name != "":
            customer = Customer.objects.filter(name__icontains=name).first()
            try:
                self.display_customer_info_for_edit(customer)
            except:
                return
        elif email != "":
            customer = Customer.objects.filter(email__icontains=email).first()
            try:
                self.display_customer_info_for_edit(customer)
            except:
                return
        elif mobile != "":
            customer = Customer.objects.filter(mobile__icontains=mobile).first()
            try:
                self.display_customer_info_for_edit(customer)
            except:
                return
        else:
            self.addCustomer_editCompany_lineEdit.setText("")
            self.addCustomer_editName_lineEdit.setText("")
            self.addCustomer_editPhone_lineEdit.setText("")
            self.addCustomer_editEmail_lineEdit.setText("")


    def display_customer_info_for_edit(self,customer):
        self.addCustomer_editCompany_lineEdit.setText(customer.company)
        self.addCustomer_editName_lineEdit.setText(customer.name)
        self.addCustomer_editPhone_lineEdit.setText(customer.mobile)
        self.addCustomer_editEmail_lineEdit.setText(customer.email)
        self.customer_id = customer.id

    def add_customer_btn_clicked(self):
        name=self.addCustomer_addName_lineEdit.text()
        company=self.addCustomer_addCompany_lineEdit.text()
        mobile=self.addCustomer_addPhone_lineEdit.text()
        email=self.addCustomer_addEmail_lineEdit.text()
        if Customer.objects(company=company):
            QtWidgets.QMessageBox.critical(self.tab_3, "Duplicate", "Company Already Exits")
        else:
            add_customer(name=name,company=company,mobile=mobile,email=email)
            QtWidgets.QMessageBox.about(self.tab_3, "Success", "Cutomer Added")
        self.reset_diplay_customer_combobox()

    def addPhone_AddButtonClicked(self):
        model = self.addPhone_model_comboBox.currentText()
        storage = self.addPhone_storage_comboBox.currentText()
        color = self.addPhone_color_comboBox.currentText()
        grade = self.addPhone_grade_comboBox.currentText()
        imei = self.addPhone_imei_lineEdit.text()
        full_name = model + " " + storage + "GB [" + grade + " Grade] [" + color +"]"
        if self.addPhone_productID_lineEdit.text() == "":
            try:
                   product_id = Phone.objects.filter(Q(full_name=full_name)&Q(product_id__exists=True)).first().product_id
            except:
                product_id = ""
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
                self.display_new_phones_in_newPhone_table()
                self.display_updated_phones_in_summary_table()
                
            #display new phone in table below

    def display_new_phones_in_newPhone_table(self):
        self.addPhone_tableWidget_displayAddedPhones.setRowCount(0)
        self.new_phone_list = list(Phone.objects(input_confirmed=False).order_by("-date_modified"))
        for phone in self.new_phone_list:
            row = self.new_phone_list.index(phone)
            self.addPhone_tableWidget_displayAddedPhones.insertRow(row)
            self.addPhone_tableWidget_displayAddedPhones.setItem(row,0,QtWidgets.QTableWidgetItem(str(phone.product_id)))
            self.addPhone_tableWidget_displayAddedPhones.setItem(row,1,QtWidgets.QTableWidgetItem(str(phone.full_name)))
            self.addPhone_tableWidget_displayAddedPhones.setItem(row,2,QtWidgets.QTableWidgetItem(str(phone.imei)))
            delete_btn = QtWidgets.QPushButton("Delete")
            self.addPhone_tableWidget_displayAddedPhones.setCellWidget(row,3,delete_btn)
            delete_btn.clicked.connect(self.delete_btn_clicked)

    def delete_btn_clicked(self):
        delete_btn = QtWidgets.QApplication.focusWidget()
        index = self.addPhone_tableWidget_displayAddedPhones.indexAt(delete_btn.pos())
        if index.isValid():
            #set change_check status to True
            phone_id = self.new_phone_list[index.row()].id
            Phone.objects(id=phone_id).delete()
            self.display_new_phones_in_newPhone_table()

    def display_fullname_and_imei(self,full_name,imei):
        self.addPhone_displayFullName_label.setText(full_name)
        self.addPhone_displayIMEI_label.setText(imei)		

    def display_updated_phones_in_summary_table(self):
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
            #set change_check status to True
            full_name = self.addPhone_newQty_tableWidget.item(index.row(),1).text()
            Phone.objects(full_name=full_name).update(change_checked=True)
            self.display_updated_phones_in_summary_table()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = InventoryApp(MainWindow)
MainWindow.show()
app.exec_()