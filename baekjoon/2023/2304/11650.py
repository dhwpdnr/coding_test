case = int(input())
arr = []
for _ in range(case):
    xy = list(map(int, input().split()))
    arr.append(xy)

arr.sort()

for i in arr:
    print(i[0], i[1])
