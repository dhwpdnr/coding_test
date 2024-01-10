case = int(input())

arr = []

for _ in range(case):
    s = list(map(str, input().split()))
    s = s[2:] + s[:2]
    arr.append(" ".join(s))

for i in arr:
    print(i)
