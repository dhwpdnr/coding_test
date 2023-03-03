def solution(a, b, n):
    answer = 0
    while (n >= a):
        coke, n = divmod(n, a)
        answer += coke * b
        n += coke * b
    return answer

    # 프로그래머스 연습문제 콜라 문제