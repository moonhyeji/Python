import re


#split
str01 = 'Hello, world!\nhello, python!'
print(str01)

arr01 = str01.split(' ') #공백기준으로 잘라줌 
print(arr01)

arr02 = str01.split(' ',1) #공백으로 자를건데 한번만 잘라줘.
print(arr02)

arr03 = re.split('[\s]|[,]', str01)
print(arr03)

#join
arr04 = ['1','2','3','4']
print(arr04)
print('+'.join(arr04))
print(eval('+'.join(arr04)))   #eval함수: 실제로 실행 







