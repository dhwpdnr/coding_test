import sys

input = sys.stdin.readline
n = int(input())
answer = 0
cows = {}
for _ in range(n):
    number, location = input().split()
    if number in cows:
        if cows[number] != location:
            answer += 1
    cows[number] = location

print(answer)
