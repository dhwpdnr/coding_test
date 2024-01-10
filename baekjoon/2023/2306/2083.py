answers = []

while True:
    name, age, kg = map(str, input().split())
    if name == "#":
        break
    if int(age) > 17 or int(kg) >= 80:
        answers.append(f"{name} Senior")
    else:
        answers.append(f"{name} Junior")

for answer in answers:
    print(answer)
