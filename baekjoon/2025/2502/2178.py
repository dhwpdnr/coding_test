import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(N)]


def bfs(si, sj, ei, ej):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))  # 시작점
    v[si][sj] = 1  # 시작점 방문 표시

    while q:
        ci, cj = q.pop(0)

        # 종료 조건
        if (ci, cj) == (ei, ej):
            return v[ci][cj]

        # 4방향 탐색
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위 내에 있고, 길이 있고, 방문하지 않았다면
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


answer = bfs(0, 0, N - 1, M - 1)
print(answer)
