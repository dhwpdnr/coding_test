n = int(input())

for i in range(n):
    print(" " * i + "*" * (n - 1 - i) + "*" + "*" * (n - 1 - i))
for i in range(n - 1):
    print(" " * (n - 2 - i) + "*" * (i + 1) + "*" + "*" * (i + 1))
