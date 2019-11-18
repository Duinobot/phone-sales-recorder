import datetime
from mongoengine import *

#a list of imei number will be stored in customer instance.

class Customer(Document):
    name = StringField(required = True)
    company = StringField(required = True)
    phone = StringField()
    email = StringField()
    imei = ListField(ReferenceField(Imei))
    