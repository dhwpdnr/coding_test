n = int(input())

for i in range(n, 1, -1):
    print(" " * (i - 1) + "*" * (n - i) + "*" + "*" * (n - i))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (i - 1) + "*" + "*" * (i - 1))
