from pymongo import MongoClient


client = MongoClient("mongodb+srv://fepinzon77:evGZFj7y0nP5znTG@clusterfpg.6b9mwdo.mongodb.net/?retryWrites=true&w=majority")

db = client.contactsdb

collection_number = db["numero_collection"]
