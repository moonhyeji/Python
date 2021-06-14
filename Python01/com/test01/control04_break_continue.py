i = 1

while i <= 10:
    if i > 5:
        break
    print(i)
    i+= 1
    
else:
    print('i:', i)
    #반복문 else구문추가할 수 있지만 정상종료 됐을 때는작동하고, break를 통해 탈출했을 때는 출력되지 않는다.
    
print('----------')

for i in range(1, 10):
    if i%2 == 0:
        continue   #실행하지 않고 다음 반복문으로 감. 
    print(i)
else:
    print('i:',i)
    
    #1,3,5,7,9    i: 9