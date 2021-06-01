#tuple : list와 거의 같다.  ()형태로배열이 만들어진다.



#생성자 사용 
a = tuple()
print(a)
b = tuple([1,2,'3'])
print(b)


#tuple은 값을 변경,추가할 수 없다. (추가 수정 삭제 불가)
#a.append(1)
print(a)
#b[1] ='2'  #TypeError: 'tuple' object does not support item assignment

print('------------')
#()사용
d = tuple(range(3,6))
print( 'print(d) : ' + d)
print(b + d)

#tuple -> list
e = list(d) 
e.append(6)
print(e)


#list -> tuple
f = tuple(e)
print(f)


#unpacking
g, h, i, j = f
print(g)
print(h)
print(i)
print(j)



















