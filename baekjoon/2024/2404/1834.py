n = int(input())

sum = 0

if n != 0 or n != 1:
    for i in range(1, n):
        sum += i * n + i

print(sum)
