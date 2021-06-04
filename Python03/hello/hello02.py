# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')     # @는... 클래스 공부 해야알 수 있음. 이름은'데코레이터'
def root():
    return '<h1><a href="/flask">hello, Flask</a></h1>'


@app.route('/flask')
def hello_flask():
    return '<h1>go <a href="/">root</a></h1>'

if __name__ == '__main__':
    app.run()
    
    
    #1.hello.Flast(link) 출력 -> go 'root(link)'출력 
    #root 클릭하면  href="/" 에 의해서 다시 hello.Flask(link)로 이동 