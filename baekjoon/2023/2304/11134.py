case = int(input())

answer = []

for _ in range(case):
    a, b = map(int, input().split())
    c, d = divmod(a, b)
    if d:
        answer.append(c + 1)
    else:
        answer.append(c)
for i in answer:
    print(i)
