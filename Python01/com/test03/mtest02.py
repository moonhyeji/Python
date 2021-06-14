def func01(x, y):
    return x + y

def func02(x, y):
    return x+y, x-y  #값이 여러개가 들어가있으면 일반적으로 튜플로 나옴 (11, -3)
    
def func03(x,y):
    print('{}, {} 두개가 입력되었습니다.'.format(x,y))
    print('%d + %d = %d'%(x,y,x+y))

if __name__ == '__main__':
    print(func01(1,3))        #4
    print(func02(4,7))        #(11,-3)    
    
     
    print(type(func02(4,7)))  #tuple
    
    #print붙이면 리턴되는값이 없다고 뜸.
    func03(6,8)