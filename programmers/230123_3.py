def solution(my_string):
    answer = ''
    for i in my_string :
        if i.isupper():
            answer += i.lower()
        else :
            answer += i.upper()
    return answer

    # 프로그래머스 연습문제 대문자와 소문자