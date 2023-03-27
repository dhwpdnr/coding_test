n, money = map(int, input().split())
coins = []

for _ in range(n):
    n = int(input())
    coins.append(n)

coins.sort(reverse=True)
answer = 0
for coin in coins:
    if money // coin >= 1:
        i, money = divmod(money, coin)
        answer += i

print(answer)
