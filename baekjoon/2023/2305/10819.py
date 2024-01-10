from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

per_arr = permutations(arr)

answer = 0

for i in per_arr:
    sum = 0
    for k in range(n - 1):
        sum += abs(i[k] - i[k + 1])
    if answer < sum:
        answer = sum

print(answer)
