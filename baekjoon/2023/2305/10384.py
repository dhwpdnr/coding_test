alphabet = list(range(97, 123))
case = int(input())

answers = []

for _ in range(1, case + 1):
    sentence = input().lower()
    check = [0] * 26
    for i in sentence:
        if ord(i) in alphabet:
            check[ord(i) - 97] += 1

    if min(check) == 0:
        answers.append(f"Case {_}: Not a pangram")
    elif min(check) == 1:
        answers.append(f"Case {_}: Pangram!")
    elif min(check) == 2:
        answers.append(f"Case {_}: Double pangram!!")
    elif min(check) == 3:
        answers.append(f"Case {_}: Triple pangram!!!")

for answer in answers:
    print(answer)
