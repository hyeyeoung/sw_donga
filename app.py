from flask import Flask
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('input'))

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/input_back', methods = ['POST'])
def input_back():
    hello = request.form['input']  # 요청한 값을 리스트 형태로 hello에 저장
    function(hello)   # 함수 사용
    return render_template('output.html', hello = hello)  # hello는 데이터값 동적 변수로 html에서 사용 가능(단, 플라스크는 동작해야함)

# ------------------------------------------
# 일반 함수(프로그램을 돌리면서 필요한 일반 함수들)
def function(name):
    print(name)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
