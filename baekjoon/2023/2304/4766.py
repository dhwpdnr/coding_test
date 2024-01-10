arr = []

while True:
    temp = float(input())
    if temp == 999:
        break
    else:
        arr.append(temp)

for i in range(len(arr) - 1):
    print("{:.2f}".format(arr[i + 1] - arr[i]))
