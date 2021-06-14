# -*- coding:utf-8 -*-

#pip install pymongo
# : preferencies → python Interpreters→ manage with pip → install python입력 →run클릭 →send클릭 

from pymongo import MongoClient

#client연결 : 둘중에 아무거나 써도 됨.
client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')

#------여기까지가 terminal에 #mongo 라고 친 상태, 연결되어있는 상태


#db연결 : 둘중에 아무거나 써도 됨.
db = client.test
#db = client['test']


#collection연결 
collection = db.score
#collection = db['score']



result = collection.find()
#print(result)


for res in result:
    print(res)
    
    
    
    
    
    
    
    
    
    
    
    
