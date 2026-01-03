from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") 

#admin database
db = client.admin

#Linked_Insights collection
pages_collection = db.Linked_Insights

