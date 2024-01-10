arr = []

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    else:
        arr.append([a // b, a % b, b])

for i in arr:
    print(f"{i[0]} {i[1]} / {i[2]}")
