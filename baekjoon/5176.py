case = int(input())
answer = []
for _ in range(case):
    people, chair = map(int, input().split())
    arr = []
    for __ in range(people):
        n = int(input())
        arr.append(n)
    set_arr = set(arr)
    answer.append(len(arr) - len(set(arr)))

for i in answer:
    print(i)
