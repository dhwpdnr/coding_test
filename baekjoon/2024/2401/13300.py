from collections import Counter

n, k = map(int, input().split())
arr = []
for _ in range(n):
    s, y = input().split()
    arr.append(s + y)

counter = Counter(arr)
answer = 0
for i in counter:
    a, b = divmod(counter[i], k)
    answer += a + (1 if b != 0 else 0)
print(answer)
