def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []
    for index, val in enumerate(answers):
        if val == a[index % len(a)]:
            score[0] += 1
        if val == b[index % len(b)]:
            score[1] += 1
        if val == c[index % len(c)]:
            score[2] += 1

    for idx, i in enumerate(score):
        if i == max(score):
            answer.append(idx + 1)
    return answer

    # 프로그래머스 연습문제 모의고사
