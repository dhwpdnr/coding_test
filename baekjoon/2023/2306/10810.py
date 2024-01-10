n, m = map(int, input().split())

basket = [0] * n

for _ in range(m):
    start, end, number = map(int, input().split())
    for i in range(start - 1, end):
        basket[i] = number

print(" ".join(map(str, basket)))
