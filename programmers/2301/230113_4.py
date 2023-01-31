def solution(n, s):
    answer = []
    if s < n:
        answer = [-1]
    else :
        k = s // n
        for i in range(n):
            answer.append(k)
        a = s % n
        for t in range(a):
            answer[t] = answer[t] + 1
        answer.sort()
    return answer

    # 프로그래머스 최고의 집합
