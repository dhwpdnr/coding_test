case = int(input())

answer = []

for _ in range(case):
    n = int(input())
    n2 = int(str(n)[::-1])
    n3 = n + n2
    if str(n3) == str(n3)[::-1]:
        answer.append("YES")
    else:
        answer.append("NO")

for i in answer:
    print(i)
