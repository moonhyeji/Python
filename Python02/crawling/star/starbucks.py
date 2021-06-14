# -*- coding:utf-8 -*-
#firefox 가 DOM 탐색에는 편하다! 

import requests
import json 
 
def getSiDo():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)
    
    #print(resp.json()['list'][0])
    sido_json = resp.json()['list']
    sido_code = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    #print(sido_code) 
    #print(sido_name)
    
    sido_dict = dict(zip(sido_code, sido_name))
    #print(sido_dict)
    return sido_dict

if __name__ == '__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해주세요 : ')
    
    
    
    
    
    
    