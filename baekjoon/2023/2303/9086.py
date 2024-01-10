case = int(input())
arr = []
for _ in range(case):
    a = str(input())
    arr.append(a[0] + a[-1])
for i in arr:
    print(i)
