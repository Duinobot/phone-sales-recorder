import datetime
from mongoengine import *
from data.imei import *

#a list of imei number will be stored in customer instance.

class Customer(Document):
    name = StringField(required = True)
    company = StringField(required = True,unique=True)
    mobile = StringField()
    email = StringField()