from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

password = os.environ.get("MONGO_PWD")

db_con_string = f"mongodb+srv://mapioli:{password}@mapcluster.yrx3nsf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_con_string)

### SETUP ###

# listing all the databases within the cluster.
dbs = client.list_database_names()
#print(dbs)

# accessing the mapioli database.
mapioli_db = client.mapdb

# lisitng collections within the database.
mapped_collections = mapioli_db.list_collection_names()
#print(mapped_collections)


def insert_hike_doc(hike_t, hike_c):
    collection = mapioli_db.mapped
    # creating a document where our hike data will be stored.
    mapped_document = {
        "trail": hike_t,
        "coordinates": hike_c 
    }
    # adding the document that was just created to the collection.
    collection.insert_one(mapped_document)

def delete_hike_doc():
    collection = mapioli_db.mapped
    # sorting the documents in descending order
    sorted_docs = collection.find().sort("_id", -1)
    # retrieve the first document from the sorted list (most recent added document).
    latest_document = sorted_docs[0]
    # delete most recently added document.
    collection.delete_one({"_id": latest_document["_id"]})

    