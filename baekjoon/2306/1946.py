# 시간 초과

case = int(input())
answers = []
for _ in range(case):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort()

    cnt = 1
    max_score = arr[0][1]
    for i in range(1, n):
        if max_score > arr[i][1]:
            cnt += 1
            max_score = arr[i][1]

    answers.append(cnt)

for answer in answers:
    print(answer)

# 시간초과 개선

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    result = 1

    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1

    print(result)
