# -*- coding:utf-8 -*-
#python에서의 인코딩 방법~!




#__ 가 붙은 변수들은 내부에서만 사용되는, 외부에 보여줄 필요가 없는 변수구나! 
     #private 과 비슷하다고 생각 !  


def func01():      #def: 함수다 라고 정의해 주는 애.
    print('함수01 입니다.')
    
def func02():
    return '함수02 입니다.'

def func03():
    return   {1:"qclass", 2:"화이팅"}




#main: 프로그램의 주 진입점!
if __name__ == '__main__':
    print('프로그램 시작 시 가장 먼저 호출됨!')
    func01()
    print(func02()) 
    print(func03())
    print(func03()[1])
    
    
    
    
    
    
    
    
    
    
    