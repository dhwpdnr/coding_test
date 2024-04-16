x, y = input().split()
arr = []
for i in range(int(x)):
    arr.append(list(map(str, input())))

a = 0
for i in range(int(x)):
    if "X" not in arr[i]:
        a += 1
b = 0
for j in range(int(y)):
    if "X" not in [arr[i][j] for i in range(int(x))]:
        b += 1

print(max(a, b))
