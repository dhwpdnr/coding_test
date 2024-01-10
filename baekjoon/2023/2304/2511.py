card_a = list(map(int, input().split()))
card_b = list(map(int, input().split()))

if card_a == card_b:
    print("10 10")
    print("D")
else:
    score_a = 0
    score_b = 0
    record = ""
    for a, b in zip(card_a, card_b):
        if a > b:
            score_a += 3
            record = "A"
        elif a < b:
            score_b += 3
            record = "B"
        else:
            score_a += 1
            score_b += 1
    print(score_a, score_b)
    if score_a > score_b:
        print("A")
    elif score_a < score_b:
        print("B")
    else:
        print(record)
