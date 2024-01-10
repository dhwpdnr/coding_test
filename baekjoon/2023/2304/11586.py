case = int(input())
arr = []
for _ in range(case):
    arr_input = str(input())
    arr.append(arr_input)
angry = int(input())

if angry == 1:
    for i in arr:
        print(i)
if angry == 2:
    for i in arr:
        print(i[::-1])
if angry == 3:
    for i in range(case - 1, -1, -1):
        print(arr[i])
