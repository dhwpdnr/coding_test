case = int(input())
answer = []

for _ in range(case):
    num = int(input())
    people = [int(input()) for i in range(num)]
    max_vote = max(people)
    index = people.index(max_vote)
    del people[index]
    if max_vote in people:
        answer.append("no winner")
    elif max_vote > sum(people):
        answer.append(f"majority winner {index + 1}")
    else:
        answer.append(f"minority winner {index + 1}")

for k in answer:
    print(k)
