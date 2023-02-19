def solution(phone_number):
    answer = []
    for i in phone_number[0:-4]:
        answer.append("*")
    return ''.join(s for s in answer) + phone_number[-4:]

    # 프로그래머스 연습문제 핸드폰 번호 가리기

def solution(phone_number):
    return  "*"*len(phone_number[0:-4]) + phone_number[-4:]

    # 간단한 풀이