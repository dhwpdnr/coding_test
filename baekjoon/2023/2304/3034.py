case, w, h = map(int, input().split())

test = (w ** 2 + h ** 2) ** 0.5

answer = []

for _ in range(case):
    n = int(input())
    if n > test:
        answer.append("NE")
    else:
        answer.append("DA")

for i in answer:
    print(i)
