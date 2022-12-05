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
    return render_template('guid.html')

@app.route('/input')
def input():
    return render_template('input.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        req = request.form # <class 'werkzeug.datastructures.ImmutableMultiDict'> 이렇게 하면 req의 key는 form의 name 속성값, req는 해당 name 속성값의 태그에서 입력된 값
        # ex. req['relation']처럼 name 속성으로 접근하면 된다.

        # idx = dict() # 주연배우(?)랑 숫자 인덱스랑 매치된 dictionary. key: 주연배우, value: 인덱스
        rel_object = req['relation']
        rel_object = Syntax_object_fun(rel_object)
        if type(rel_object) is list:
            r = makeIdx(req['relation'])
            idx = r[0]
            idx2 = r[1]
            tmp = r[2]
            acti = r[3]
            
            print(idx)
            # relation, capacity 초기화
            # relation은 모든 주연배우를 key로 가지며 value는 주연배우의 크기만큼인 배열을 False로 채운다
            # capactity는 모든 주연배우를 key로 가지며 value는 빈 리스트이다.

            if len(acti) != 1:
                return render_template('output.html', value={'error': 'more than one activation subject or no activation subject'})

            activationSubject = acti[0]
            relation = makeRelation(req['relation'], idx, tmp)
            capacity = makeCapacity(req['code'], idx)
            
            print("activationSubject: " + activationSubject)
            print('== relation ==')
            print(relation)
            print('== capacity ==')
            print(capacity)

            result = []
            for c in capacity[activationSubject]:
                result = isConnected(activationSubject, idx2, relation, capacity, c, [])
            if not result:
                result.append('false')
                result.append(activationSubject + ' has no request. This is not service.')

            print(result)
            # isgoodCode(activationSubject, idx, relation, capacity)

            # 활성화 주체(rel_object)부터 모든 존재하는 관계를
             
            return render_template('output.html', value=result)
        mes = 'Syntax Error!: '+ rel_object
        return render_template('error.html', error = mes)
    mes = 'input error! please retry'
    return render_template('error.html', error = mes)

if __name__ == '__main__':
    app.debug = True
    # debug=True 없이 기본으로 실행하면 수정 사항을 반영하기 위해 서버를 재기동해야 한다.
    app.run(debug=True)
