coin_arr = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]
case = int(input())

answers = []

for _ in range(case):
    coin_try = str(input())
    check = []
    for coin in coin_arr:
        count = 0
        for i in range(38):
            if coin == coin_try[i:i + 3]:
                count += 1
        check.append(count)
    answers.append(check)

for answer in answers:
    print(" ".join(map(str, answer)))
