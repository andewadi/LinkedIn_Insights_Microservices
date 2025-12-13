from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")  # Use your URI if different

# Use your admin database
db = client.admin

# Use the Linked_Insights collection
pages_collection = db.Linked_Insights

