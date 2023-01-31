def solution(sides):
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        return 1
    return 2

    # 프로그래머스 연습문제 삼각형의 완성조건(1)