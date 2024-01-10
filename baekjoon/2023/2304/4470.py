case = int(input())

arr = []

for _ in range(case):
    arr.append(str(input()))

for index, item in enumerate(arr):
    print(f"{index + 1}. {item}")
