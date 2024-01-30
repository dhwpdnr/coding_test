import sys

input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr = arr[::-1]
top = arr[0]
answer = 1
for i in arr:
    if i > top:
        answer += 1
        top = i

print(answer)
