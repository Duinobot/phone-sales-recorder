from mongoengine import *
import pymongo
#connect database with pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client.learning_mongo
#connect database with mongoengine
connect('learning_mongo')

try:
    add_phone(imei="test",model="test",storage="test",color="test",grade="test")
except:
    pass