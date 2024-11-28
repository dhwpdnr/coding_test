import sys

input = sys.stdin.readline
N = int(input())
result = 1
for i in range(1, N + 1):
    result *= i
    while result % 10 == 0:
        result //= 10
    result %= 100_000_000_000

result %= 10
print(result)
