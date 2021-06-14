# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.test  #test라는 db.
collection = db.score  #score라는 collection

# res01 = collection.insert_one({'name': '???', 'kor':56, 'eng': 87, 'math':100})
# print(res01.inserted_id)



res02 = collection.insert_many(
     [
         {'name':'아이언맨', 'kor': 48, 'eng':100, 'math':64},
         {'name':'캡틴', 'kor': 17, 'eng':94, 'math':100},
         {'name':'호크아이', 'kor': 100, 'eng': 88, 'math':91}   
     ]
 ) 

print(res02.inserted_ids)

for doc in collection.find():
    print(doc)
    



