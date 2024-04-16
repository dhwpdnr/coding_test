arr = list(map(int, input().split()))

arr.sort()
i = arr[0]
while True:
    cnt = 0
    for num in arr:
        if i % num == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break
    i += 1
