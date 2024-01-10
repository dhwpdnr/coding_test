case = int(input())

answers = []

for _ in range(case):
    n = int(input())
    str_out = "Pairs for " + f"{n}:"
    for i in range(1, n // 2 + 1):
        if i != n - i:
            if i != 1:
                str_out += ","
            str_out += f" {i} {n - i}"
    answers.append(str_out)

for answer in answers:
    print(answer)
