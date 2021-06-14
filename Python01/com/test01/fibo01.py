# n = input('input n: ')  #1  #input = 넣어준 숫잣값 가지고 옴  
#print(n)         #1  
#print(type(n))   #<class 'str'>


#fibonacci 수열 : 0 1 1 2 3 5 8 13 21 34 55 89...
n = input('숫자입력 : ')


a, b = 0, 1
i= 0
while i  < int(n) :
    print(a , end='')
    a,b = b, a+b
    i += 1
    print()
    
    #반복할 숫자 입력 
    #python의 swap -> a,b = b,a 
    


res=list()
a,b =0,1
i= 0
while i < int(n):
    res.append(a)
    a, b = b, a+b
    i += 1
print(res)  #여기서 print에 탭이 들어가 있으면 추가되는 숫자 하나하나 다 배열안에 들어가게 됨.
    
    
    