case = int(input())

dp = [1, 2, 4, 7]

answers = []

for _ in range(case):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[-3] + dp[-2] + dp[-1]) % 1000000009)
    answers.append(dp[n - 1])

for answer in answers:
    print(answer)
