def solution(t, p):
    answer = 0
    for i in range(0, len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1
    return answer

    # 프로그래머스 연습문제 크기가 작은 부분 문자열