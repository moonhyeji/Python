# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.test
collection = db.score


#이름이 ???인 애 지우기 
res01 = collection.delete_one({'name':'???'})
print(res01.deleted_count)


#test field가 존재하는 모든 document를 삭제하자.
res02 = collection.delete_many({'test':{'$exists':True}})
print(res02.deleted_count)

#모든 document들을 삭제하자.
collection.delete_many({})