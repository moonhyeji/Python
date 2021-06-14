# -*- coding:utf-8 -*-

with open('test01.txt','r') as file:  #file = open('test01.txt','r')
    a = file.read()
    print(a)
            #file.close() 없어짐 --close 안해도 자동으로 하게 해주는것 = with as.