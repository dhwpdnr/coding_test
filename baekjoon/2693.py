case = int(input())
answer = []

for _ in range(case):
    arr = list(map(int, input().split()))
    arr.sort()
    answer.append(arr[-3])

for i in answer:
    print(i)
