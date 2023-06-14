arr = [[0] * 100 for i in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2-1):
        for j in range(y1 - 1, y2-1):
            arr[i][j] = 1
answer = 0
for x in arr:
    answer += x.count(1)

print(answer)
