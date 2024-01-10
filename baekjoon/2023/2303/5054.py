case = int(input())
result = []
for _ in range(case):
    shop = int(input())
    shop_arr = list(map(int, input().split()))
    result.append((max(shop_arr) - min(shop_arr)) * 2)
for i in result:
    print(i)
