N = int(input())
S, E = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(S, E):
    queue = []
    visited = [0] * (N + 1)
    queue.append(S)
    visited[S] = 1

    while queue:
        c = queue.pop(0)

        if c == E:
            return visited[c] - 1
        for n in graph[c]:
            if not visited[n]:
                queue.append(n)
                visited[n] = visited[c] + 1
    return -1


answer = bfs(S, E)
print(answer)
