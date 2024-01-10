n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

answer = roads[0] * costs[0]
money = costs[0]
distance = 0

for i in range(1, n - 1):
    if costs[i] < money:
        answer += money * distance
        distance = roads[i]
        money = costs[i]
    else:
        distance += roads[i]

    if i == n - 2:
        answer += money * distance

print(answer)
