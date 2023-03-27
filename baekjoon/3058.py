case = int(input())
sum_arr = []
min_arr = []

for _ in range(case):
    arr = list(map(int, input().split()))
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
    sum_arr.append(sum(even))
    min_arr.append(min(even))
for sum_num, min_num in zip(sum_arr, min_arr):
    print(sum_num, min_num)
