#set = 집합  (중복안됨, 순서없음)

#생성자
a = set(['1','2','3','4','1'])
print(a)


#iterable(반복가능한) (java: 반복해서 비교해주는 애)
#생성자에 iterable(반복가능)한 객체를 넣으면 set의 값으로 변환 
b = set('hello')
print(b)   #반복해서 하나씩 가져와서 값으로 가짐 

#{}사용
c = {'a','b','c','hello','1','2','3'}
print(c)

#추가 
c.add('world')
print(c)


#합집합/ 교집합
print(a.union(b))
print(a|b)

print(a.intersection(c))
print(a & c)


























