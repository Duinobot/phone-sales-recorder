import datetime
from mongoengine import *

class Phone(Document):
    imei = StringField(required = True)
    
    full_name = StringField()
    model = StringField(required = True)
    storage = StringField(required = True)
    color = StringField(required = True)
    grade = StringField(required = True)
    product_id = StringField()
    
    date_in = DateTimeField(required=True, default = datetime.datetime.now())
    date_out = DateTimeField()
    date_modified = DateTimeField(required=True, default = datetime.datetime.now())
    change_checked = BooleanField(required=True, default = False)
    customer_id = ObjectIdField()
    