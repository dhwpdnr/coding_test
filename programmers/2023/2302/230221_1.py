def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

    # 프로그래머스 연습문제 내적


def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])

    # 리스트 컴프리헨션과 zip 사용
