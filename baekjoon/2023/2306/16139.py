# 50 점

s = input()
case = int(input())
for _ in range(case):
    find, start, end = map(str, input().split())
    start = int(start)
    end = int(end)
    print(s[start:end + 1].count(find))

# 100점
import sys

input = sys.stdin.readline

s = input().rstrip()
arr = [[0] * 26]
arr[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i]) - 97] += 1

for _ in range(int(input())):
    c, start, end = list(input().split())
    start, end = map(int, [start, end])
    if start == 0:
        print(arr[end][ord(c) - 97])
    else:
        print(arr[end][ord(c) - 97] - arr[start - 1][ord(c) - 97])
