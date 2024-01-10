n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))
for _ in range(n):
    arr2.append(list(map(int, input().split())))
answer = []
for i, k in zip(arr1, arr2):
    arr = []
    for j in range(m):
        arr.append(i[j] + k[j])
    answer.append(arr)
for a in answer:
    print(" ".join(map(str, a)))
