arr = [[0] * 100 for i in range(100)]

case = int(input())

for _ in range(case):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[x + i][y + j] = 1

answer = 0
for i in arr:
    answer += i.count(1)
print(answer)
