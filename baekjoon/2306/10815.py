n = int(input())
cards = set(list(map(int, input().split())))
m = int(input())
check_arr = list(map(int, input().split()))

for i in check_arr:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
