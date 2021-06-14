# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='


resp = requests.get(url)
#가져오기 get방식으로 요청해서 .
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup)

#soup.select('dd ul li p') 도 같은 값이 나온다.

inner_value = soup.find_all(class_='inner_value')
#print(inner_value)
 
 
 
#여러줄 문자열
result = '''국내발생 : {}      
해외유입 : {}
소   계 : {}
'''.format(inner_value[1].text, inner_value[2].text, inner_value[0].text.split('')[1])
print(result)


















