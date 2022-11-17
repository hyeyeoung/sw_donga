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
    r = []
    ret = dict()
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

        if tmp[i][1][0] == '(':
            tmp[i][1] = tmp[i][1].replace('(', '')
            tmp[i][1] = tmp[i][1].replace(')', '')

        if tmp[i][0] not in ret:
            ret[tmp[i][0]] = cnt
            cnt = cnt + 1
        if tmp[i][1] not in ret:
            ret[tmp[i][1]] = cnt
            cnt = cnt + 1
    r.append(ret)
    r.append(tmp)
    return r

def makeRelation(req, idx, tmp):
    ret = {}
    for key in idx.keys():
        ret[key] = [False for i in range(len(idx.keys()))]
    
    for i in range(len(tmp)):
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

if __name__ == '__main__':
    a = "coffee <-> tester, test <-> buyer) "
    Syntax_object_fun(a)