def solution(lines):
    table = [0 for i in range(200)]
    for line in lines:
        for i in range(line[0], line[1]):
            table[i + 100] += 1

    return len([i for i in table if i >= 2])

    # 프로그래머스 연습문제 겹치는 선분의 길이