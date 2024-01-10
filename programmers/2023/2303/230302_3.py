from itertools import combinations


def solution(numbers):
    com_list = list(combinations(numbers, 2))
    answer = []
    for i in com_list:
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    return answer

    # 프로그래머스 연습문제 두개 뽑아서 더하기
