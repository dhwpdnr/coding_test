def solution(n):
    answer = 0
    num = n ** 0.5

    if num == int(num):
        answer = (num+1) ** 2
    else:
        answer = -1

    return answer

    # 프로그래머스 연습문제 정수 제곱근 판별