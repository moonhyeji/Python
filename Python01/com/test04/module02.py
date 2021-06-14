#pip install numpy       -> 수치해석, 숫자(배열 행렬....) 와 관련된 모듈,(라이브러리)
#pip install matplotlib  -> 시각화(그래프)

#별칭 지어주기 가능,numpy 는 보통 np 로 이용중!
import numpy as np  
import matplotlib.pyplot as plt 
import random


def plt01():
    x = np.range(0,11)
    y = x
    #print(x)
    #print(y)
    
    
    plt.plot(x,y)
    plt.xlabel('x')
    plt.xlabel('y')
    
    plt.legend(['y=x'])
    
    plt.show()


def plt02():
    x = [random.randint(0,10)for _ in range(10)]
    y = range(10)
    plt.bar(x, y)
    plt.xticks(range(11))
    plt.yticks(range(11))
    plt.show()
    
    
def plt03():
    data = [random.randint(100, 1000) for _in range(4)]
    plt.pie(data)
    
    category = ['first','second','third','fourth']
    plt.legend(category)
    
    plt.show()
    
#-----------------
if __name__ == '__main__':
    #plt01()
    #plt02()
    plt03()