from collections import deque

case = int(input())

answers = []

for _ in range(case):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            count += 1
            if m < 0:
                answers.append(count)
                break

        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1

for answer in answers:
    print(answer)
