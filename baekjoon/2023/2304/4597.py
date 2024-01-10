answer = []

while True:
    n = str(input())
    if n == "#":
        break
    else:
        parity = n[-1]
        n = n[:-1]
        if parity == "e":
            if n.count("1") % 2 == 0:
                answer.append(n + "0")
            else:
                answer.append(n + "1")
        else:
            if n.count("1") % 2 == 0:
                answer.append(n + "1")
            else:
                answer.append(n + "0")

for i in answer:
    print(i)
