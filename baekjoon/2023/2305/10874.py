case = int(input())
arr = []
answer = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

for _ in range(case):
    test = list(map(int, input().split()))
    if test == answer:
        arr.append(_ + 1)

for i in arr:
    print(i)
