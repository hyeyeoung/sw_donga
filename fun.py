# 함수 파일
# ----------------------------------------------

# 앞 뒤에 콤마가 있는지 확인하는 함수, 만약 앞 뒤에 함
# 간단한 파싱 후 이상 없으면 객체 리스트 리턴
# 추후 할 일은? 객체 리스트와 textarea input의 매칭 
def Syntax_object_fun(input_object):
    # 제일 앞 뒤에 쉼표가 존재하는지?
    if ord(input_object.strip()[-1]) == ord(',') or ord(input_object.strip()[0]) == ord(','):
        input_object = "error: comma"
        return input_object
    # 제일 마지막 객체를 활성화 객체라고 가정함
    # 간단한 문법 에러 한 번 거른 후 리스트로 나누기    
    if ord(input_object.strip()[-1]) != ord(')'):
        input_object = "error: input"
        return input_object
    # 콤마를 기준으로 각 객체간의 관계를 1차적으로 나눠준다.
    # 최종 결과 리스트 선언
    input_object_list = input_object.split(',')
    result_object_list = []
    # 객체 내에 관계가 없다면 그 관계는 틀린 것
    for i in input_object_list:
        if "<->" not in i:
            input_object = "error: relationship"
            return input_object
        else: # 최종적으로 관계에 따라 문자열을 나눠준다
            a = i.split("<->")
            if a[0] not in result_object_list: # 기존 리스트에 객체가 존재하는지 확인
                result_object_list.append(a[0]) 
            if a[1] not in result_object_list: 
                result_object_list.append(a[1])
    # 마지막이 활성화 객체/ 활성화 객체의 첫 시작이 괄호인지 확인
    if "(" != result_object_list[-1].strip()[0]:
        input_object = "error: activation object"
        return input_object 
    return result_object_list


if __name__ == '__main__':
    a = "coffee <-> tester, test <-> buyer) "
    Syntax_object_fun(a)