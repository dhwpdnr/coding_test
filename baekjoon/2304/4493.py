case = int(input())

answer = []

for _ in range(case):
    n = int(input())
    win_1 = 0
    win_2 = 0
    for __ in range(n):
        p1, p2 = map(str, input().split())
        if p1 == "R":
            if p2 == "P":
                win_2 += 1
            elif p2 == "S":
                win_1 += 1
        elif p1 == "S":
            if p2 == "R":
                win_2 += 1
            elif p2 == "P":
                win_1 += 1
        elif p1 == "P":
            if p2 == "S":
                win_2 += 1
            elif p2 == "R":
                win_1 += 1

    if win_1 > win_2:
        answer.append("Player 1")
    elif win_1 < win_2:
        answer.append("Player 2")
    else:
        answer.append("TIE")

for i in answer:
    print(i)
