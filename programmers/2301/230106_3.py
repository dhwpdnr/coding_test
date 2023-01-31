def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "0" :
            answer += "5"
        elif i == "2":
            answer += "0"
        elif i == "5":
            answer += "2"
    return answer

    # 프로그래머스 연습 문제