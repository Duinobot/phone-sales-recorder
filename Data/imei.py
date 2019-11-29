import datetime
from mongoengine import *
from Data.customer import *

class Imei(EmbeddedDocument):
    imei_no = StringField(required = True, unique=True,)
    customer_id = ObjectIdField()
    Date_in = DateTimeField(default=datetime.datetime.now)
    Date_out = DateTimeField(default=datetime.datetime.now)
    