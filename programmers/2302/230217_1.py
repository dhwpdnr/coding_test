def solution(a, b):
    answer = 0
    if a > b:
        large = a
        small = b
    else:
        large = b
        small = a
    for i in range(small, large + 1):
        answer += i
    return answer

    # 프로그래머스 연습문제 두 정수 사이의 합


def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        answer += i
    return answer

    # 크기 비교를 간단하게 줄인 케이스
