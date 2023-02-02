from itertools import combinations
from fractions import Fraction

def solution(dots):
    temp = set()
    for dot1, dot2 in combinations(dots,2):
        inc = Fraction(dot1[1] - dot2[1], dot1[0] - dot2[0])
        if inc in temp:
            return 1
        temp.add(inc)
    return 0

    # 프로그래머스 연습문제 평행