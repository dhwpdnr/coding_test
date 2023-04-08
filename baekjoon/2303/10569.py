case = int(input())
arr = []
for _ in range(case):
    v, e = map(int, input().split())
    arr.append(e - v + 2)
for i in arr:
    print(i)
