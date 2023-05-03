answers = []

while True:
    born_min, born_max, dead_min, dead_max = map(int, input().split())
    if born_min == 0 and born_max == 0 and dead_min == 0 and dead_max == 0:
        break
    answers.append([dead_min - born_max, dead_max - born_min])

for answer in answers:
    print(answer[0], answer[1])
