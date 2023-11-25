from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://Ivan:malivajo@cluster0.tue7chl.mongodb.net/?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]

post = {"_id" :1, "name": "ok"}

collection.insert_one(post)