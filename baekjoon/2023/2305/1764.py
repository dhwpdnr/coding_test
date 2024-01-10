from collections import Counter

n, m = map(int, input().split())

arr = [input() for _ in range(n + m)]

counter = Counter(arr)
answers = []

for key, value in counter.items():
    if value == 2:
        answers.append(key)

answers.sort()

print(len(answers))
for answer in answers:
    print(answer)
