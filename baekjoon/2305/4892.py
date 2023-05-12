number = 0
answers = []
while True:
    n = int(input())
    number += 1
    if n == 0:
        break
    if n % 2 != 0:
        answers.append(f"{number}. odd {n // 2}")
    else:
        answers.append(f"{number}. even {n // 2}")

for answer in answers:
    print(answer)
