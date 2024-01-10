from itertools import permutations

case = int(input())
num_list = list(map(int, input().split()))

cal = ["+", "-", "*", "//"]
cal_list = []

cal_number = list(map(int, input().split()))
total_cal_number = sum(cal_number)
for i in range(4):
    if cal_number[i] != 0:
        for k in range(cal_number[i]):
            cal_list.append(cal[i])

cal_case = list(permutations(cal_list, len(cal_list)))
answer = []

for case in cal_case:
    result = num_list[0]
    for k in range(total_cal_number):
        if case[k] == "+":
            result += num_list[k + 1]
        elif case[k] == "-":
            result -= num_list[k + 1]
        elif case[k] == "*":
            result *= num_list[k + 1]
        else:
            if result < 0:
                result = -(abs(result) // num_list[k + 1])
            else:
                result = result // num_list[k + 1]
    answer.append(result)

print(max(answer))
print(min(answer))
