'''
*
**
***
****
*****
'''
a = 1
while a <= 5:
    for b in range(a):
        print("*", end="")
    a += 1
    print()
print('-------------')
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()
print('-------------')
for i in range(5):
    print('*' * (i + 1))
'''
*****
****
***
**
*
'''
print('-------------')
for i in range(5):
    print('*' * (5 - i))

'''
    *
   **
  ***
 ****
*****
'''
print('-------------')
for i in range(5):
    print(' ' * (4 - i), '*' * (i + 1))
'''
*****
 ****
  ***
   **
    *
'''
print('-------------')
for i in range(5):
    print(' ' * i, '*' * (5 - i))
'''
    *
   ***
  *****
 *******
*********
'''
print('-------------')
for i in range(5):
    print(' ' * (4 - i), '*' * ((i * 2) + 1))