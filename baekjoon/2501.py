num, k = map(int, input().split())

answer = []
for i in range(1, num + 1):
    if num % i == 0:
        answer.append(i)

try:
    print(answer[k - 1])
except IndexError:
    print(0)
