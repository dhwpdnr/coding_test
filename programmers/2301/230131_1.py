def solution(dots):
    dots.sort()
    answer = (dots[1][1] - dots[0][1]) * (dots[3][0]-dots[0][0])
    return answer

    # 프로그래머스 연습문제 직사각형 넓이 구하기