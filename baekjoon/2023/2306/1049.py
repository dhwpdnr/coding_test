n, m = map(int, input().split())
price = []
for _ in range(m):
    price.append(list(map(int, input().split())))

six_list = sorted(price, key=lambda x: x[0])
six_price = six_list[0][0]
one_list = sorted(price, key=lambda x: x[1])
one_price = one_list[0][1]

if six_price <= one_price * 6:
    answer = six_price * (n // 6) + one_price * (n % 6)
    if six_price < one_price * (n % 6):
        answer = six_price * (n // 6 + 1)
else:
    answer = one_price * n

print(answer)
