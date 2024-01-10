from itertools import permutations

N = int(input())

res = permutations(range(1, N + 1), N)

for perm in res:
    print(" ".join(map(str, perm)))
