n = int(input())
arr = set(list(map(int, input().split())))

m = int(input())
check_arr = list(map(int, input().split()))

for i in check_arr:
    if i in arr:
        print(1)
    else:
        print(0)
