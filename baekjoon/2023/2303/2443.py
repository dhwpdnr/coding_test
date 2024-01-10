num = int(input())

for i in range(num, 0, -1):
    print(" " * (num - i) + "*" * (i - 1) + "*" + "*" * (i - 1))
