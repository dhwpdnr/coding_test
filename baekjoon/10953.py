case = int(input())
answer = []

for _ in range(case):
    a, b = map(int, input().split(","))
    answer.append(a + b)

for i in answer:
    print(i)
