import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(len(sys.stdin.readline().rstrip()))

dict = defaultdict(int)

count = 0

for end in range(n):

    if (end > k):
        dict[arr[end - k - 1]] -= 1

    count += dict[arr[end]]

    dict[arr[end]] += 1

print(count)
