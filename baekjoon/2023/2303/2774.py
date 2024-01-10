case = int(input())
answer = []
for _ in range(case):
    a = str(input())
    a = list(set(list(a)))
    answer.append(len(a))

for i in answer:
    print(i)
