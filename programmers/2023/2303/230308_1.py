def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        fruit = score[i:i + m]
        if len(fruit) == m:
            answer += fruit[-1] * m
    return answer

    # 프로그래머스 연습문제 과일 장수
