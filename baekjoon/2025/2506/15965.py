INF = 10 ** 7

k = int(input())
array = [1 for _ in range(INF + 1)]

answer = []
for i in range(2, INF + 1):
    if array[i]:
        answer.append(i)
        for j in range(i + i, INF + 1, i):
            array[j] = 0

print(answer[k - 1])
