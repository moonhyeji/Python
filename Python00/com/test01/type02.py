#문자

#single quot* 1
a = 'python\'s\nHello, world!'
print(a)
print('----------------')


#single quot * 3
b = '''python's
Hello, world!
    hello python!
       hello Qclass
'''
print(b)       


print('---double quot *1 -----------')
#double * 1
c = "abc\"def\"ghi"
print(c)

print('\t')
print('---double quot *3 -----------')
#double *3
d = """abc    "def"  ghi"""
print(d)

e='abc"def"ghi\npython\'s string'
print(e)

f="abc'def'ghi\npython's stirng"
print(f)


print('\t')
print('---raw string -----------')
#r(raw) string
g = r"c:\test"    #(raw) string 은 '\'를 문자로 인식 
print(g)

h="c:\test"
print(h)



print('\t')
print('---str 연산 ----------')
#str 연산 
str01 ="Hello,"
str02 ="World"

print(str01 + str02)
print(str01 *3 + str02)











