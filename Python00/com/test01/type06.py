#dictionary  k=v 한 쌍 

# (): tuple  / []:list/ {} :set / {k ;v} :dictionary
#dic은 자바의 map처럼  순서가 없고, key 는 중복 안되는데 v는 중복 가능,


#생성자
dict01 = dict()
dict01[1] =1
dict01[2] ='2'
print(dict01)


# {}로 생성 
dict02 = {}
dict02['one'] =1 
dict02[2] = 'this is two'
dict02[3] = 1
print(dict02)

#key를 통해서 value 가져오기 
print(dict01.get(2))
print(dict02['one'])

print(dict01.keys())
print(dict02.values())

#keys를 list안으로 넣어서, 1번 인덱스의 값 가져오기 
print('\n#keys를 list안으로 넣어서, 1번 인덱스의 값 가져오기 :  ')
print(list(dict01.keys())[1])








