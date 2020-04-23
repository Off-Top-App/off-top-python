from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import datetime

# connect to MongoDB
#To establish a connection to MongoDB with PyMongo you use the MongoClient class
client = MongoClient('mongodb://localhost:27017/')
#create a database object referencing a new database, called “newDB”
#A single instance of MongoDB can support multiple independent databases.
#MongoDB stores flexible JSON-like documents
with client:
    db = client.newDB
#Creating a test collection which is a group of documents roughly the equivalent of a table in a relational database
    collection1= db.test_collection
    collectionList= db.list_collection_names()
    if "customers" in collectionList:
        print("The collection exists.")
# Issue the serverStatus command and print the results
    serverStatusResult = db.command("serverStatus")
    #status = db.command("dbstats")
    print(collectionList)
    #db.collection_names() is depreciated
    pprint(serverStatusResult)
