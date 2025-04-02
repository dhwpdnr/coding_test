# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 공원 산책
# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    x, y = 0, 0
    w, h = len(park[0]), len(park)
    op = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x, y = i, j
                break

    for r in routes:
        d, n = r.split(" ")
        dx, dy = x, y

        for i in range(int(n)):
            nx = x + op[d][0]
            ny = y + op[d][1]

            if 0 <= nx <= h - 1 and 0 <= ny <= w - 1 and (park[nx][ny] != "X"):
                x, y = nx, ny

            else:
                x, y = dx, dy
                break

    return [x, y]


q = solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])
assert q == [2, 1]
print(q)

q = solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"])
assert q == [0, 1]
print(q)

q = solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"])
assert q == [0, 0]
print(q)
