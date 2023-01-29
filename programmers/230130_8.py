def solution(sides):
    sides.sort()
    answer = 0
    i = sides[1] - sides[0] + 1
    while i <= sides[1]:
        answer += 1
        i += 1
    k = sides[1] + 1
    while k < sides[0] + sides[1]:
        answer += 1
        k += 1
    return answer

    # 프로그래머스 연습문제 삼각형의 완성조건(2)


def another(sides):
    sides.sort()
    return sides[0] * 2 - 1


    # 위와 같은 식으로도 결과 값이 나온다