def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer

    # 프로그래머스 연습문제 약수의 합