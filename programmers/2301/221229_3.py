def solution(slice, n):
    i = 1
    while True :
        if i*slice >= n :
            return i
        i += 1
    # 프로그래머스 코딩테스트 입문