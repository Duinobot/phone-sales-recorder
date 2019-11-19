from typing import List, Optional
import datetime
import bson
from data.customer import Customer
from data.imei import Imei
from data.phone import Phone
from mongoengine.queryset.visitor import Q

#0 find phone in database
# take attribute as input and look for the device, if not exist use 
# #2 add phone to database 
def find_phone_in_database(model=model,storage=storage,
                           color=color,grade=grade) -> Phone:
    #TODO: find phone
    If phone = Phone.objects(model=model,storage=storage,color=color,grade=grade):
    else:
        phone = add_phone_to_database(model=model,storage=storage,color=color,grade=grade)
    return phone


# add imei to database
def add_imei_to_phone(imei_no=imei_no,phone=phone) -> Imei:
    new_imei = Imei(imei_no=imei_no, phone=phone, Date_in=datetime.datetime.now())
    #how to save embeded document
    phone.imei = 
    return new_imei

#2 add phone to database
def add_phone_to_database(model=model,storage=storage,color=color,grade=grade) -> Phone:
    #TODO: need to add full name of phone
    new_phone = Phone(model=model, storage=storage, color=color, grade=grade)

#3 display_modified_inventory
def display_modified_inventory

#4 modified status change
def modified_status -> Boolean:
    
#5 display by date_modified
def display_by_date_modified

#6 search by imei
def search_by_imei

#7 search for customer
def search_for_customer

#8 add customer
def add_customer

#9 aissgn customer to imei
def imei_sold


