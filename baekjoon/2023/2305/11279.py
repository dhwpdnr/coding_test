import heapq

case = int(input())

heap = []
answers = []

for _ in range(case):
    n = int(input())
    if n == 0:
        try:
            answers.append(-1 * heapq.heappop(heap))
        except:
            answers.append(0)
    else:
        heapq.heappush(heap, -n)

for answer in answers:
    print(answer)

# 시간 초과 해결

import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1) * heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1) * m)
