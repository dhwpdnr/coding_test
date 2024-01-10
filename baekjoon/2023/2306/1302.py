from collections import Counter

case = int(input())
arr = []
for _ in range(case):
    arr.append(input())

arr = Counter(arr)

arr = sorted(arr.items())

max = 0
max_book = ""
for i in arr:
    if i[1] > max:
        max = i[1]
        max_book = i[0]
print(max_book)
