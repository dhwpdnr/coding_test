def solution(n):
    answer = 0
    i = 1
    while i <= n :
        if i % 2 == 0:
            answer += i
        i += 1
    return answer

    # 프로그래머스 연습 문제
