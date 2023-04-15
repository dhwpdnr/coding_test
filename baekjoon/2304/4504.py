num = int(input())
arr = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr.append(n)

for i in arr:
    if i % num == 0:
        print(f"{i} is a multiple of {num}.")
    else:
        print(f"{i} is NOT a multiple of {num}.")
