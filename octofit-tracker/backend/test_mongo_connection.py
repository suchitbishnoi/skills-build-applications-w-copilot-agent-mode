import pymongo
from pymongo.errors import ConnectionFailure

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017/"

try:
    # Establish a connection to MongoDB
    client = pymongo.MongoClient(MONGO_URI)
    # Access the octofit_db database
    db = client["octofit_db"]

    # List collections
    collections = db.list_collection_names()
    print("Collections in octofit_db:", collections)
except Exception as e:
    print(f"An error occurred while listing collections: {e}")
