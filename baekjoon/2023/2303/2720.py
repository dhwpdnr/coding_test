case = int(input())
answer = []
for _ in range(case):
    money = int(input())
    quarter, money = divmod(money, 25)
    dime, money = divmod(money, 10)
    nickel, money = divmod(money, 5)
    penny, money = divmod(money, 1)
    answer.append([quarter, dime, nickel, penny])

for i in answer:
    print(" ".join(map(str, i)))
