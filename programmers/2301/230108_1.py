import math


def solution(balls, share):
    n = math.factorial(balls)
    n_m = math.factorial(balls - share)
    m = math.factorial(share)

    return n / (n_m * m)

    # 프로그래머스 연습 문제