case = int(input())

A = 65

answer = []

for _ in range(case):
    front, back = map(str, input().split("-"))
    front = (ord(front[0]) - A) * 26 * 26 + (ord(front[1]) - A) * 26 + (ord(front[2]) - A)
    if abs(front - int(back)) <= 100:
        answer.append("nice")
    else:
        answer.append("not nice")

for i in answer:
    print(i)
