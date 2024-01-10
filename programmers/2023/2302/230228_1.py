from itertools import combinations


def solution(number):
    answer = 0
    com_list = list(combinations(number, 3))
    for i in com_list:
        if sum(i) == 0:
            answer += 1
    return answer

    # 프로그래머스 연습문제 삼총사
