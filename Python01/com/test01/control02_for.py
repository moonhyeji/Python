#from numpy.lib.function_base import average
subject = ['java', 'javascript','python']
for s in subject:
    print(s, end=' ')
else:
    print('재밌다.')
#java javascript python 재밌다.

print('---------')
for i in range(1, 100):
    print(i, end=' ')
    
print('\n---------')
print('구구단')

for i in range(2, 10):
    print('[ ' + str(i) + '단 ]')
    for j in range(2, 10):
        print(str(i) + 'x' + str(j) + '=' + str(i*j))
       # print(i, 'x', j, '=', j*j, sep = '')
    print()
    
    print('------------------')
    
    
#range 함수 이용해서 10~1 까지 거꾸로 출력 
for i in range(10, 0, -1):
    print(i , end=' ')
    
    