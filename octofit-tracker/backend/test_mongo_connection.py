import pymongo
from pymongo.errors import ConnectionFailure

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017/"

try:
    # Establish a connection to MongoDB
    client = pymongo.MongoClient(MONGO_URI)
    # Send a ping to verify the connection
    client.admin.command('ping')
    print("MongoDB is running and accessible.")
except ConnectionFailure as e:
    print(f"MongoDB connection failed: {e}")
