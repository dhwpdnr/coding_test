case = int(input())

answer = []

for _ in range(case):
    legs, chicken = map(int, input().split())
    for i in range(chicken + 1):
        if i * 2 + (chicken - i) == legs:
            answer.append([chicken - i, i])
            break

for t in answer:
    print(t[0], t[1])
