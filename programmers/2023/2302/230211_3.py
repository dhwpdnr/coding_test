def solution(numlist, n):
    return sorted(numlist, key = lambda x: (abs(x - n), -x))

    # 프로그래머스 연습문제 특이한 정렬