case = int(input())

arr = []
for _ in range(case):
    x, y = map(int, input().split())
    yx = [y, x]
    arr.append(yx)

arr.sort()

for i in arr:
    print(i[1], i[0])
