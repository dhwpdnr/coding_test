arr = [int(input()) for _ in range(28)]

answer = []

for i in range(1, 31):
    if i not in arr:
        answer.append(i)

answer.sort()

print(answer[0])
print(answer[1])
