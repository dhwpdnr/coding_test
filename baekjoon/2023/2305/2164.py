from collections import deque

n = int(input())

arr = [i for i in range(1, n + 1)]
arr = deque(arr)

while len(arr) > 1:
    arr.popleft()
    a = arr.popleft()
    arr.append(a)

print(arr[0])
