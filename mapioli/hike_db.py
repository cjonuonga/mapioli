from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

password = os.environ.get("MONGO_PWD")

db_con_string = f"mongodb+srv://mapioli:{password}@mapcluster.yrx3nsf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_con_string)

### SETUP ###

# listing all the databases within the cluster
dbs = client.list_database_names()
#print(dbs)

# accessing the mapioli database
mapioli_db = client.mapdb

# lisitng collections within the database
mapped_collections = mapioli_db.list_collection_names()
#print(mapped_collections)

def insert_hike_doc(hike_t, hike_c):
    collection = mapioli_db.mapped
    mapped_document = {
        "trail": hike_t,
        "coordinates": hike_c 
    }

    collection.insert_one(mapped_document)