# -*- coding:utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    html = '''
    <h1>GET/POST</h1>
    <a href='/test'>get</a>
    <form action='/test' method='post'>
        <input type='submit' value='post'>
    </form>
    '''
    return html



@app.route('/test', methods=['GET','POST'])  #test로 왔을 때 받아주겠다.
def hello_test():
    if request.method == 'POST':
        return '<h1 style="color:orange">Request post</h1>'
    else:
        return '<h1 style="color:skyblue">Request get</h1>'
    
    
if __name__=='__main__':
    app.run()
    
    
    