from collections import Counter

case = int(input())

arr = []
for _ in range(case):
    arr.append(int(input()))

arr = Counter(arr)
result = sorted(arr.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
