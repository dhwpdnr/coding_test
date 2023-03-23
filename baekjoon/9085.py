case = int(input())
arr = []
for _ in range(case):
    a = int(input())
    n_list = list(map(int, input().split()))
    arr.append(n_list)
for i in arr:
    print(sum(i))
