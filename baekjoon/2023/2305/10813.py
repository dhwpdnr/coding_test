N, case = map(int, input().split())

basket = [i for i in range(1, N + 1)]
temp = 0

for i in range(case):
    i, j = map(int, input().split())
    temp = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = temp

print(" ".join(map(str, basket)))
