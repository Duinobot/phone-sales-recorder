import datetime
from mongoengine import *

class Imei(EmbeddedDocument):
    imei = StringField(required = True)
    customer = ReferenceField(Customer)
    Date_in = DateTimeField(default=datetime.datetime.now)
    Date_out = DateTimeField(default=datetime.datetime.now)