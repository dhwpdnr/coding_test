def solution(n):
    ans = 0
    while n > 0 :
        if n % 2 == 0 :
            n = n / 2
        else:
            n = n - 1
            ans += 1
    return ans

    #  프로그래머스 점프와 순간이동