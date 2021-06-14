def coffee(quantity, price):
    change = price - (quantity * 100)
    if change >= 0: 
        prn(quantity,change)
    else:
        prn()


def prn(quantity=0, change=0):  # 파라미터 값이 들어오지 않으면 기본값은 0 이다 라고 지정해줌. 
    if quantity == 0 & change == 0 : 
        print('돈이 부족합니다.')
    else:
        print('커피 {}잔이 나왔습니다.\n 잔돈은 {}원 입니다.'.format(quantity,change))
    pass

def start():
    q = int(input('커피 몇잔 드릴까요?'))
    p = int(input('돈 주세요! (1잔당 100원)'))
    coffee(q, p)
    
    
if __name__ == '__main__': 
    start()
     #'__name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행하라.