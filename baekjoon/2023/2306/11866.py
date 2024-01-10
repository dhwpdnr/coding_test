from collections import deque

n, k = map(int, input().split())

queue = deque(x for x in range(1, n + 1))

k_1 = k - 1

answer = []

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<" + ", ".join((map(str, answer))) + ">")
