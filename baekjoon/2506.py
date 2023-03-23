n = int(input())
answer = list(map(int, input().split()))
sum = 0
score = 0
for index, num in enumerate(answer):
    if index > 0:
        if num == 1:
            score += 1
            sum += score
        else:
            score = 0
    else:
        if num == 1:
            score += 1
            sum += score
        else:
            score = 0
print(sum)