case = int(input())

a = 0
b = 1

for _ in range(case - 1):
    a, b = b, a + b
print(a, b)
