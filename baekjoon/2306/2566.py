arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))
num, x, y = 0, 0, 0

for i in range(9):
    for j in range(9):
        if num < arr[i][j]:
            x = i
            y = j
            num = arr[i][j]

print(num)
print(x + 1, y + 1)
