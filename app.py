from fun import *
from flask import Flask
from flask import Flask, render_template, request, session, redirect, url_for
# render_template 함수는 flask에서 제공하는 함수로 templates에 저장된 html을 불러올 때 사용하는 함수이다.

app = Flask(__name__)


# flask에서는 decorator가 URL 연결에 사용된다. 다음 행의 함수부터 decorator가 적용된다.
@app.route('/')
def hello_world():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        value = request.form
        rel_object = value['object']
        rel_object = Syntax_object_fun(rel_object)
        if type(rel_object) is list:
            req = request.form
            r = makeIdx(req['object'])
            idx = r[0]
            tmp = r[1]
            
            print(idx)
            relation = makeRelation(req['object'], idx, tmp)
            capacity = makeCapacity(req['code'], idx)
            
            print('== relation ==')
            print(relation)
            print('== capacity ==')
            print(capacity)
            return render_template('output.html', value=req)
    return render_template('output.html', value=rel_object)

if __name__ == '__main__':
    app.debug = True
    # debug=True 없이 기본으로 실행하면 수정 사항을 반영하기 위해 서버를 재기동해야 한다.
    app.run(debug=True)
