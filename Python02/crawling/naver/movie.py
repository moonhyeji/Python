# -*- coding:utf-8 -*-

#pip install beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request
from _ast import Attribute

#요청해서 응답받아오려는 경로 넣기 

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
#print(resp)         #response 객체 넘어오는 것 확인 
soup = BeautifulSoup(resp, 'html.parser')

#print(soup)  #파싱된 document 객체 .(dom 탐색한 응답받은 객체)

movies = soup.find_all('dl', class_='lst_dsc')
#print(movies)

#--------------------------------------------
#movies 안에 있는 제목과 별점을 parsing 해서  제목 [별점] 으로 반복해서 출력하자.
for movie in movies:
    #print(movie)
    title = movie.find('a').text
    star = movie.find('span',class_='num').text
    print('{} [{}]'.format(title, star))
    #print(title)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    