arr = [int(input()) for _ in range(7)]
answer = []
for i in arr:
    if i % 2 != 0:
        answer.append(i)
if len(answer) > 0:
    answer.sort()
    print(sum(answer))
    print(answer[0])
else:
    print(-1)
