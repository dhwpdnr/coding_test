from collections import deque

dw = [-1, -1, -1, 0, 0, 1, 1, 1]
dh = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(graph, h, w):
    queue = deque()
    queue.append((h, w))
    while queue:
        h, w = queue.popleft()
        for i in range(8):
            nw = w + dw[i]
            nh = h + dh[i]
            if 0 <= nw < len(graph[0]) and 0 <= nh < len(graph) and graph[nh][nw] == 1:
                graph[nh][nw] = 0
                queue.append((nh, nw))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    cnt = 0
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)
