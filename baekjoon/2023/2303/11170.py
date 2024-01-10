case = int(input())
arr = []
for _ in range(case):
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b + 1):
        count += str(i).count("0")
    arr.append(count)

for k in arr:
    print(k)
