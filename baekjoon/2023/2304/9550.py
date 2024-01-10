case = int(input())

answer = []

for _ in range(case):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    for i in arr:
        count += i // k
    answer.append(count)

for k in answer:
    print(k)
