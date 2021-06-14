# -*- coding:utf-8 -*-

#pip install requests
from bs4 import BeautifulSoup
import requests
import json


url='https://comic.naver.com/webtoon/weekdayList.nhn?week=thu'
resp = requests.get(url)


#print(resp.text)   # --res.text는 문자열객체 
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)   #-- 태그 하나하나가(ex.</script>) 객체화되어 내가 원하는 것만 잘라서 올 수있음.

#제목[별점]


img_list = soup.find('ul',class_='img_list')

webtoons = img_list.select('dl')

lst = list()
for webtoon in webtoons:
    title = webtoon.find('a')['title']
    star = webtoon.find('strong').text
    print('{} [{}]'.format(title, star))
    tmp = {}   #dic   #{}는 set or dictionary
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)
    

#print(lst)
res = {}
res['webtoons'] = lst
res_json = json.dumps(res, ensure_ascii=False) #한글인코딩 
print(res_json)

with open('webtoons.json','w',encoding='utf-8') as f:          #파일로 저장
    f.write(res_json) 

