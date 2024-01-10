def solution(n):
    answer = 0
    i = 1
    while i <= n :
        if n % i == 0 :
            answer+=1
        i += 1
    return answer

    # 프로그래머스 연습문제