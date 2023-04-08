num = int(input())
answer = []
for i in range(num):
    calc = list(map(str, input().split()))
    n = float(calc[0])
    for cal in calc:
        if cal == "@":
            n *= 3
        elif cal == "%":
            n += 5
        elif cal == "#":
            n -= 7
    answer.append(n)
for i in answer:
    print("{:.2f}".format(i))
