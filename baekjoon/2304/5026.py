case = int(input())

answer = []

for _ in range(case):
    try:
        a, b = map(int, input().split("+"))
        answer.append(a + b)
    except:
        answer.append("skipped")

for i in answer:
    print(i)
