x, y = map(int, input().split())
result = 1
while x != y:
    result += 1
    temp = y
    if y % 10 == 1:
        y = y // 10
    elif y % 2 == 0:
        y = y // 2
    if temp == y:
        print(-1)
        break
else:
    print(result)
