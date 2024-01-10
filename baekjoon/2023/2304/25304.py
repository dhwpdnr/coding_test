money = int(input())

case = int(input())

pay = 0

for _ in range(case):
    price, n = map(int, input().split())
    pay += price * n

if pay == money:
    print("Yes")
else:
    print("No")
