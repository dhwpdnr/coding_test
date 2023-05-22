from itertools import permutations

case = int(input())
num_list = list(map(int, input().split()))

cal = ["+", "-", "*", "//"]
cal_list = []

cal_number = list(map(int, input().split()))

for i in range(4):
    if cal_number[i] != 0:
        for k in range(cal_number[i]):
            cal_list.append(cal[i])

cal_case = list(permutations(cal_list, len(cal_list)))

print(cal_case)
