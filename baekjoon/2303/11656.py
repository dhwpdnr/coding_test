input_str = str(input())
arr = []
for i in range(len(input_str)):
    arr.append(input_str[i:])
arr.sort()
for k in arr:
    print(k)
