#산술연산
a = 21
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a ** b) #a^b  441
print(a / b)
print(a // b)  #몫 (floor division - 소수점 이하는 버린다.)
print(a % b)



#비교연산
a, b = 5, 3 #a에 5가 들어가고 b 에 3이 들어감 
print('\n  ***a =5, b=3 일 때의 연산*** ')
print(a == b)
print(a != b)
print(a > b)
print(a <= b)
print(a is b)
print(a is not b)
print('-------------')

print(True or True)
print(True or False)
print(False or True)
print(False and False)
print(not False)
print('-------------')

#범위연산
# 0부터 n전까지 만들어줌. 
#range(n) : 0 ~ < n
list01 = list(range(100))  # 0 ~ 99
print(list01)

print(list01[2])         #2
print(list01[12:49])     #12 ~48
print(list01[12:49:3])   #12,15,18,21..(3씩증가)


#[start: end] -> start ~ end -1
#[start: end: step] ->start ~ end -1 까지 step만큼 증가 

print('----hello world---------')
str01 = 'hello, world!'
print(str01)
print(str01[0:5])
print(str01[:5])  # : 의 앞이 생략되면 처음 
print(str01[7:])  # : 뒤가 생략되면 끝까
print(str01[7:-1])  #world
print(str01[7:12])  #world
print(str01[:4]*3)


print('----reverse---------')
#reverse
print(str01[-1])
print(str01[-6:])
print(str01[:-1])
print(str01[::-1])

print('------member연산----')
#멤버연산
list02 = [0, 1, 2, 3, 4]
print(3 in list02)
print(5 in list02)
print(5 not in list02)























