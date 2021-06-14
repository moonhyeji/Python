'''
def hap01(a,b):
    return a+b


--자바스크립트처럼 작성한다면, 
hap01 = function(a,b){
    return a+b
}

hap01(10,20)
'''
hap01 = lambda a,b: a + b
print(hap01(10,20))

hap02 = lambda a,b,c: a+b+c
print(hap02(30,40,50))

gob = lambda a,b : a*b
print(gob(12,34))


a = [(1, 'one',9),(2, 'two',8),(3, 'three',7),(4,'four',6)] #list안에 튜플 여러개 넣음. list[(숫자,영어,숫자)]
print(a)
#sort(내가 정렬할 값들을 가져옴 여기서는 [])
a.sort(key=lambda a: a[1])  #lambda a: a[1] = 영어기준으로 정렬하자.
      # a라는 거 받아서 하나하나 가져올 건데 a의 1번지에 있는 값들 기준으로 정렬해 줄 것이다.
      
print(a)

min01 = lambda x,y:  x if x < y else y   # if 조건이 참일 때 if x < y  이면 x를, 거짓일 때 y를 리턴.
print(min01(33,44))



max01 = lambda x,y : x if x > y else y 
print(max01(55,66))

print('----------')

#변수 = lambda 변수정의 : 변수활용(숫자넣기) 
b = lambda x: (lambda newx: x + newx)  #익명함수 생성 , x에 값을 넣어주면 안에 익명함수가 또 있으니까 또 실행 
print(b(100)(200))
c = b(100)
# c= lambda newx:100 + newx
print(c)
d = c(200)
# d= lambda newx: 100 + 200   //결과값 300
print(d)


#1~100 사이의 5의 배수 출력 
e = lambda x: bool(x%5)
five = [i for i in range(1,101) if not e(i)]   #x를 5로나눈 나머지가 0 이 아닌 애들이 아님. = 5의 배수인 애들만 출력해라.
       #^ 이 i 가 리턴된다.
print(five)


f = lambda x: x if(x % 5 != 0) else None  # x 나누가 5가 0 이면 none 출력 (none = null = false)
res = [i for i in range(1,101) if not f(i)]
print(res)


#위 두개 합친 것,
result = [i for i in range(1,101) if not (lambda x : x if(x % 5 != 0) else None)(i)]




































