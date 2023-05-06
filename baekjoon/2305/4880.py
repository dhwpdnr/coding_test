answers = []

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    elif b - a == c - b:
        answers.append(f"AP {c + (c - b)}")
    elif b // a == c // b:
        answers.append(f"GP {c * (c // b)}")

for answer in answers:
    print(answer)
