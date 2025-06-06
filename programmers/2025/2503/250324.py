# 프로그래머스
# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    row_len = len(maps)
    vec_len = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs():
        queue = deque()
        queue.append((0, 0))

        while queue:
            row, vec = queue.popleft()
            if (row, vec) == (row_len - 1, vec_len - 1):
                return maps[row][vec]
            for (y, x) in zip(dy, dx):
                new_row = row + y
                new_vec = vec + x
                if new_row < 0 or new_row >= row_len or \
                        new_vec < 0 or new_vec >= vec_len or \
                        maps[new_row][new_vec] == 0 or \
                        (maps[new_row][new_vec] != 1 and
                         maps[new_row][new_vec] <= maps[row][vec] + 1):
                    continue
                maps[new_row][new_vec] = maps[row][vec] + 1
                queue.append((new_row, new_vec))
        return -1

    return bfs()


q = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
assert q == 11
print(q)

q = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]])
assert q == -1
print(q)
