lines = int(input())

arr = []

for _ in range(lines):
    arr.append(list(map(int, input().split())))

for i in range(1, lines):
    for k in range(len(arr[i])):
        if k == 0:
            arr[i][k] = arr[i][k] + arr[i - 1][k]
        elif k == len(arr[i]) - 1:
            arr[i][k] = arr[i][k] + arr[i - 1][k - 1]
        else:
            arr[i][k] = max(arr[i - 1][k], arr[i - 1][k - 1]) + arr[i][k]

print(max(arr[lines - 1]))
