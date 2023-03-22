case = int(input())
arr = []
for _ in range(case):
    price = int(input())
    option_num = int(input())
    for __ in range(option_num):
        num, option_price = map(int, input().split())
        price += num * option_price
    arr.append(price)
for i in arr:
    print(i)
