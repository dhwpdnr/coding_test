price, amount, money = map(int, input().split())
need_money = price * amount - money
if need_money > 0:
    print(need_money)
else:
    print(0)
