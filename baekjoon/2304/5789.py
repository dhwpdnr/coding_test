case = int(input())

answer = []

for _ in range(case):
    a = str(input())
    len_a = len(a)
    if a[len_a // 2] == a[len_a // 2 - 1]:
        answer.append("Do-it")
    else:
        answer.append("Do-it-Not")
for i in answer:
    print(i)
