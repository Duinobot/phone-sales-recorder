from mongoengine import *

class Model:
    model = StringField(required=True)

class Storage:
    storage = StringField(required=True)
    
class Color:
    color = StringField(required=True)
    
class Grade:
    grade = StringField(required=True)