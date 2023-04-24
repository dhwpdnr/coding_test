from collections import Counter

arr = []

while True:
    input_str = str(input())
    if input_str == "*":
        break
    else:
        input_str = input_str.replace(" ", "")
        cnt = Counter(input_str)
        if len(cnt.keys()) == 26:
            arr.append("Y")
        else:
            arr.append("N")

for i in arr:
    print(i)
