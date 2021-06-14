# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint
#pprint = pretty print 


#client
client = MongoClient('localhost',27017)

#db
test = client.test

#collection
score = test.score

cursor = score.find()

for doc in cursor:
    #print(doc)
    pprint.pprint(doc)
    
print('-----  find_one  -------------')

shin = score.find_one({'name':'신동엽'})
pprint.pprint(shin)


#shin = score.find({'name':'신동엽'})
# <pymongo.cursor.Cursor object at 0x10fb89fd0>
#커서 오브젝트가 출력됨.



print('----------     국어점수가 60보다 큰 도큐먼트들을 모두 출력하자  ------------')
#국어점수가 60보다 큰 도큐먼트들을 모두 출력하자.
kor60 = score.find( {'kor' : {'$gt' :60} } )   #여기까지만 쓰면 커서 객체만 나옴.
for doc in kor60:
    pprint.pprint(doc)


print('------------- count_documents -------------------')
#document의 갯수: count_documents()
print('score collection 안에 있는 document의 총 갯수: ', score.count_documents({}))        
















