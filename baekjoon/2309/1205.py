n, x, p = map(int, input().split())
if n == 0:
    print(1)
else:
    arr = list(map(int, input().split()))
    cnt = 0
    if arr[n - 1] >= x and n == p:
        print(-1)
    else:
        for i in arr:
            cnt += 1
            if x >= i:
                print(cnt)
                break
        else:
            print(cnt + 1)
