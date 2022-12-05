# 함수 파일
# ----------------------------------------------

# 앞 뒤에 콤마가 있는지 확인하는 함수, 만약 앞 뒤에 함
def Syntax_object_fun(rel_object):
    # 제일 앞 뒤에 쉼표가 존재하는지?
    if ord(rel_object.strip()[-1]) == ord(',') or ord(rel_object.strip()[0]) == ord(','):
        rel_object = "error: comma"
        return rel_object
    # 제일 마지막 객체를 활성화 객체라고 가정함
    # 간단한 문법 에러 한 번 거른 후 리스트로 나누기    
    if ord(rel_object.strip()[-1]) != ord(')'):
        rel_object = "error: input"
        return rel_object
    # 콤마를 기준으로 각 객체간의 관계를 1차적으로 나눠준다.
    # 최종 결과 리스트 선언
    rel_object_list = rel_object.split(',')
    result_object_list = []
    # 객체 내에 관계가 없다면 그 관계는 틀린 것
    for i in rel_object_list:
        if "<->" not in i:
            rel_object = "error: relationship"
            return rel_object
        else: # 최종적으로 관계에 따라 문자열을 나눠준다
            a = i.split("<->")
            if a[0] not in result_object_list: # 기존 리스트에 객체가 존재하는지 확인
                result_object_list.append(a[0]) 
            if a[1] not in result_object_list: 
                result_object_list.append(a[1])
    # 마지막이 활성화 객체/ 활성화 객체의 첫 시작이 괄호인지 확인
    if "(" != result_object_list[-1].strip()[0]:
        rel_object = "error: activation object"
        return rel_object 
    return result_object_list




def makeIdx(req):
    ret = []
    r = dict()
    r2 = dict()
    acti = []   # 활성화 주체 목록

    tmp = req.replace(' ', '').split(',') # tmp에 관계 정보가 담김
    for i in range(len(tmp)):
        tmp[i] = tmp[i].split('-')
        tmp[i][0] = tmp[i][0].replace('<', '')
        tmp[i][1] = tmp[i][1].replace('>', '')
        
    cnt = 0
    for i in range(len(tmp)):
        if tmp[i][0][0] == '(':
            tmp[i][0] = tmp[i][0].replace('(', '')
            tmp[i][0] = tmp[i][0].replace(')', '')
            if tmp[i][0] not in acti:
                acti.append(tmp[i][0])

        if tmp[i][1][0] == '(':
            tmp[i][1] = tmp[i][1].replace('(', '')
            tmp[i][1] = tmp[i][1].replace(')', '')
            if tmp[i][1] not in acti:
                acti.append(tmp[i][1])

        if tmp[i][0] not in r:
            r[tmp[i][0]] = cnt
            r2[cnt] = tmp[i][0]
            cnt = cnt + 1
        if tmp[i][1] not in r:
            r[tmp[i][1]] = cnt
            r2[cnt] = tmp[i][1]
            cnt = cnt + 1
    ret.append(r)
    ret.append(r2)
    ret.append(tmp)
    ret.append(acti)
    return ret

def makeRelation(req, idx, tmp):
    ret = {}
    for key in idx.keys():
        ret[key] = [False for i in range(len(idx.keys()))]
    
    for i in range(len(tmp)):
        print('tmp: ', end='')
        print(tmp[i])
        ret[tmp[i][0]][idx[tmp[i][1]]] = True
        ret[tmp[i][1]][idx[tmp[i][0]]] = True
    return ret

def makeCapacity(req, idx):
    ret = {}
    for key in idx.keys():
        ret[key] = []
    
    tmp = req.replace(' ', '').split('\r\n')
    for i in range(len(tmp)):
        tmp[i] = tmp[i].split('=')
        tmp[i][1] = tmp[i][1].split(',')
        for t in tmp[i][1]:
            ret[tmp[i][0]].append(t)
    return ret

def isConnected(sub, idx, rel, capacity, target, path):
    ret = []

    if target not in capacity[sub]:
        if not ret:
            ret.append('false')
            ret.append(sub + ' has no ' + target)
        return ret

    path.append(sub)
    
    cnt = 0     # 이미 관계를 확인한 애들의 개수
    for i in range(len(rel[sub])):
        if rel[sub][i] and idx[i] not in path:
            ret = isConnected(idx[i], idx, rel, capacity, target, path)
        elif rel[sub][i]:
            cnt = cnt + 1

    all_cnt = 0     # 내가 관계가 있는 것들의 개수
    for r in rel[sub]:
        if r:
            all_cnt = all_cnt + 1

    # connected with god
    if cnt == all_cnt:      # 나와 관계가 있는 것들이 전부 이전에 봤던 것들이면 나는 god와 연결된 아이이다.
        f = target.split('>')
        if f[1] in capacity[sub] and not ret:
            ret.append('true')
        elif f[1] not in capacity[sub] and not ret:
            ret.append('false')
            ret.append(sub + ' has no capacity from GOD: ' + f[1])

    return ret
if __name__ == '__main__':
    a = "coffee <-> tester, test <-> buyer) "
    Syntax_object_fun(a)