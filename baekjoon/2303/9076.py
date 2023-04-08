case = int(input())
answer = []
for _ in range(case):
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[3] - arr[1] >= 4:
        answer.append("KIN")
    else:
        answer.append(sum(arr[1:4]))

for i in answer:
    print(i)
