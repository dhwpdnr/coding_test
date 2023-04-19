case = int(input())

answer = []

for _ in range(case):
    answer.append(sum(list(map(int, input().split()))))

for i in answer:
    print(i)
