import sys

input = sys.stdin.readline

case = int(input())

arr = []

for _ in range(case):
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i)
