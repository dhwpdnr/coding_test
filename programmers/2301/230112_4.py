def solution(n):
    i = 1
    k = n
    while 1:
        if k // i == 0:
            break
        k = k / i
        i += 1
    return i - 1

   # 프로그래머스 팩토리얼