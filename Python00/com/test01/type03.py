#list  = 배열 


#생성자
a = list()
print(a)
a.append(1)
print(a)
a.append('a')
print(a)
a[1] = 'b'
print(a)


#a[2] = 'c'
#print(a)

#[]사용
b = [1,2,3,4,5]
print(b)
print(b[0] +b[3])   #5

print('-----------------')
#list의 reverse()함수
b.reverse()
print(b)

b.append(6) 
b.sort()       #sort = 정렬 
print(b)

#중첩 
c =['a','b','c','d',['e','f','g']]
print(c)
print(c[4])
print(c[4][0])
c.append('a')



#list + list
print(b + c)

















