case = int(input())
arr = []
for _ in range(case):
    a, b = map(str, input().split())
    li = []
    for i, k in zip(a, b):
        if ord(i) > ord(k):
            li.append(26 - (ord(i) - ord(k)))
        else:
            li.append(ord(k) - ord(i))
    arr.append(li)

for t in arr:
    print("Distances:", *t)
