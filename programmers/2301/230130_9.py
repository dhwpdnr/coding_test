import re


def solution(my_string):
    numbers = re.findall(r'\d+', my_string)
    answer = 0
    for i in numbers:
        answer += int(i)
    return answer

    # 프로그래머스 연습문제 숨어있는 숫자의 덧셈
