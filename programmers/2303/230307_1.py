def solution(N, stages):
    people = len(stages)
    fail = {}
    for i in range(1, N + 1):
        if people != 0:
            fail[i] = stages.count(i) / people
            people -= stages.count(i)
        else:
            fail[i] = 0
    return sorted(fail, key=lambda x: fail[x], reverse=True)

    # 프로그래머스 연습문제 실패율