# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/181832
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 정수를 나선형으로 배치하기

def solution(n):
    answer = [[0] * n for i in range(n)]
    mode = 1
    x = 0
    y = 0

    if n == 1:
        return [[1]]
    for i in range(n * n):
        answer[x][y] = i + 1
        if mode % 4 == 1:
            y += 1
            if y == n - 1 or answer[x][y + 1] != 0:
                mode += 1
        elif mode % 4 == 2:
            x += 1
            if x == n - 1 or answer[x + 1][y] != 0:
                mode += 1
        elif mode % 4 == 3:
            y -= 1
            if y == n - 1 or answer[x][y - 1] != 0:
                mode += 1
        elif mode % 4 == 0:
            x -= 1
            if x == n - 1 or answer[x - 1][y] != 0:
                mode += 1
    return answer


q = solution(3)
assert q == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(q)

q = solution(4)
assert q == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(q)

q = solution(5)
assert q == [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
print(q)
