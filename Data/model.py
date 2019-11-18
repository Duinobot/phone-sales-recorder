from mongoengine import *
import imei

class Phone(Document):
    model = StringField(required = True)
    storage = StringField(required = True)
    color = StringField(required = True)
    grade = StringField(required = True)
    imei = ListField(EmbeddedDocumentField(Imei))
