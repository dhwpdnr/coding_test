def solution(n):
    i = 1
    while True:
        if 6*i % n == 0:
            return i
        i += 1

    # 프로그래머스 코딩테스트 입문