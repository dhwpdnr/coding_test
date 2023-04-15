case = int(input())

arr = []

for _ in range(case):
    n = str(input())
    arr.append(n)

arr = list(set(arr))

arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)
