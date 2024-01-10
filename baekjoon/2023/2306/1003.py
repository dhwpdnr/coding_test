case = int(input())

answers = []

for _ in range(case):
    N = int(input())
    zeros = [1, 0, 1]
    ones = [0, 1, 1]
    if N >= 3:
        for i in range(2, N):
            zeros.append(zeros[i - 1] + zeros[i])
            ones.append(ones[i - 1] + ones[i])
    answers.append(f"{zeros[N]} {ones[N]}")

for answer in answers:
    print(answer)
