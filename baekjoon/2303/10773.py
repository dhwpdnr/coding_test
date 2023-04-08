case = int(input())
arr = []

for _ in range(case):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)

print(sum(arr))
