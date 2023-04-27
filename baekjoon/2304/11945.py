case, n = map(int, input().split())

answer = []

for _ in range(case):
    a = str(input())
    answer.append(a[::-1])

for i in answer:
    print(i)
