state = []
people = 0
for _ in range(10):
    a, b = map(int, input().split())
    people = people - a + b
    state.append(people)
print(max(state))
