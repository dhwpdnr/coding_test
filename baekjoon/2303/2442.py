num = int(input())

for i in range(num, 0, -1):
    print(" " * (i - 1) + "*" * (num - i) + "*" + "*" * (num - i))
