num, case = map(int, input().split())

arr = [0 for i in range(num)]

for _ in range(case):
    a, b = map(int, input().split())
    arr[a - 1] += 1
    arr[b - 1] += 1

for answer in arr:
    print(answer)
