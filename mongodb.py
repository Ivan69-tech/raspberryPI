from pymongo import MongoClient

import time 


cluster = MongoClient("mongodb+srv://Ivan:malivajo@cluster0.tue7chl.mongodb.net/?retryWrites=true&w=majority")

db = cluster["test2"]
collection = db["test2"]
collection.delete_many({})
k = 0



while True :
  k += 1
  post = {"_id" :k, "name": f"{k}"}
  collection.insert_one(post)
  print(f"id {k} posté")
  time.sleep(5)

