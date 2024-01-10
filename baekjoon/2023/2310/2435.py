n, k = map(int, input().split())
temp_list = list(map(int, input().split()))
sum_list = []

for i in range(n - k + 1):
    sum_list.append(sum(temp_list[i: i + k]))

print(max(sum_list))
