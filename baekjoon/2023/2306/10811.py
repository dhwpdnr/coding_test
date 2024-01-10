n, m = map(int, input().split())

basket = [i for i in range(1, n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    temp = basket[start - 1:end]
    temp.reverse()
    basket[start - 1:end] = temp

print(" ".join(map(str, basket)))
