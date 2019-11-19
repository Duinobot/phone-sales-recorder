import datetime
from mongoengine import *

class Imei(EmbeddedDocument):
    imei_no = StringField(required = True)
    customer = ReferenceField(Customer)
    phone = ReferenceField(Phone)
    Date_in = DateTimeField(default=datetime.datetime.now)
    Date_out = DateTimeField(default=datetime.datetime.now)
    