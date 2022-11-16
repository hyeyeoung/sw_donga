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
        req = request.form # <class 'werkzeug.datastructures.ImmutableMultiDict'> 이렇게 하면 req의 key는 form의 name 속성값, req는 해당 name 속성값의 태그에서 입력된 값
        # ex. req['relation']처럼 name 속성으로 접근하면 된다.

        # 아래 코드는 req['relation']에 활성화 주체가 하나만 있다고 가정하고 작성한 코드이다.
        # ( 개수 찾아서 이게 0개나 2개 이상이면 X
        idx = dict() # 주연배우(?)랑 숫자 인덱스랑 매치된 dictionary. key: 주연배우, value: 인덱스
        tmp = req['relation'].replace(' ', '').split(',') # tmp에 관계 정보가 담김
        for i in range(len(tmp)):
            tmp[i] = tmp[i].split('-')
            tmp[i][0] = tmp[i][0].replace('<', '')
            tmp[i][1] = tmp[i][1].replace('>', '')
        
        activationSubject = '' # 활성화 주체
        cnt = 0
        for i in range(len(tmp)):
            if tmp[i][0][0] == '(':
                tmp[i][0] = tmp[i][0].replace('(', '')
                tmp[i][0] = tmp[i][0].replace(')', '')
                activationSubject = tmp[i][0]

            if tmp[i][1][0] == '(':
                tmp[i][1] = tmp[i][1].replace('(', '')
                tmp[i][1] = tmp[i][1].replace(')', '')
                activationSubject = tmp[i][1]

            if tmp[i][0] not in idx:
                idx[tmp[i][0]] = cnt
                cnt = cnt + 1
            if tmp[i][1] not in idx:
                idx[tmp[i][1]] = cnt
                cnt = cnt + 1
        
        relation = {}
        capacity = {}
        # relation, capacity 초기화
        # relation은 모든 주연배우를 key로 가지며 value는 주연배우의 크기만큼인 배열을 False로 채운다
        # capactity는 모든 주연배우를 key로 가지며 value는 빈 리스트이다.
        for key in idx.keys():
            relation[key] = [False for i in range(len(idx.keys()))]
            capacity[key] = []

        # relation 값 부여
        for i in range(len(tmp)):
            relation[tmp[i][0]][idx[tmp[i][1]]] = True
            relation[tmp[i][1]][idx[tmp[i][0]]] = True

        # capacity 값 부여
        tmp = req['code'].replace(' ', '').split('\r\n') # tmp에 모든 공백을 없앤 입력으로 들어온 능력 정보가 담김
        for i in range(len(tmp)):
            tmp[i] = tmp[i].split('=')
            tmp[i][1] = tmp[i][1].split(',')
            for t in tmp[i][1]:
                capacity[tmp[i][0]].append(t)
        
        print("activationSubject: " + activationSubject)
        print('== relation ==')
        print(relation)
        print('== capacity ==')
        print(capacity)

        # activationSubject는 relation으로부터 찾아낼 수 있다.
    return render_template('output.html', value=req)

if __name__ == '__main__':
    app.debug = True
    app.run()
    # debug=True 없이 기본으로 실행하면 수정 사항을 반영하기 위해 서버를 재기동해야 한다.
