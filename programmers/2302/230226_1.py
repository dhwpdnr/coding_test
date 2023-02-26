def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        if i <= budget:
            budget -= i
            answer += 1
        else:
            break
    return answer

    # 프로그래머스 연습문제 예산
