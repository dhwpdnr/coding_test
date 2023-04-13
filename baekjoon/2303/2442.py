num = int(input())

for i in range(1, num):
    print(" " * (num - 1 - i) + "*" * (2 * i - 1))
