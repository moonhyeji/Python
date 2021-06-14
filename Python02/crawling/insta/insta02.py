# -*- coding:utf-8 -*-

#pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup


tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

#chromedriver 아까 저장해둔 경로 
driver = webdriver.Chrome('/Users/hyejimoon/Documents/driver/chromedriver')


driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')
print(img_list)


driver.close()  #크롬창 꺼짐 
driver.quit()

