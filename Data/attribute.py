from mongoengine import *

class Attributes(Document):
    name = StringField(unique=True)
    value = ListField()
    
#initiate attribute:
try:
    Attributes(name = "model").save()
    Attributes(name = "storage").save()
    Attributes(name = "color").save()
    Attributes(name = "grade").save()
except:
    pass