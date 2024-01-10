case = int(input())
for _ in range(case):
    n = int(input())
    max = 0
    mName = ""
    for _ in range(n):
        price, name = input().split()
        price = int(price)
        if (price > max):
            max = price
            mName = name
    print(mName)
