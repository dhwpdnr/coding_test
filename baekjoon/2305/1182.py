from itertools import combinations

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

answer = 0

for i in range(1, N + 1):
    combi = combinations(num_list, i)

    for k in combi:
        if sum(k) == S:
            answer += 1

print(answer)
