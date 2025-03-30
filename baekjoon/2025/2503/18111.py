import sys

n, m, b = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
idx = 0
answer = sys.maxsize

for floor in range(257):

    max_block, min_block = 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= floor:
                max_block += graph[i][j] - floor
            else:
                min_block += floor - graph[i][j]

    if (max_block + b) >= min_block:
        if max_block * 2 + min_block <= answer:
            answer = max_block * 2 + min_block
            idx = floor
print(answer, idx)
