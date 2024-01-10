case = int(input())
answer = []

for _ in range(case):
    arr = list(map(str, input().split()))
    arr2 = []
    for k in arr:
        arr2.append(k[::-1])
    answer.append(arr2)

for i in answer:
    print(" ".join(map(str, i)))
