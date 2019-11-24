from mongoengine import *

class Attributes(Document):
    model = ListField(required=True)
    storage = ListField(required=True)
    color = ListField(required=True)
    grade = ListField(required=True)