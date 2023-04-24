from collections import Counter

case = int(input())

arr = []

for _ in range(case):
    name = str(input())
    arr.append(name[0])

cnt = Counter(arr)
cnt = cnt.items()
answer = []
for i in cnt:
    if i[1] >= 5:
        answer.append(i[0])

if answer == []:
    print("PREDAJA")
else:
    answer.sort()
    print("".join(answer))
