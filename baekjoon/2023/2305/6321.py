case = int(input())
answers = []

for _ in range(1, case + 1):
    input_str = str(input())
    out_str = ""
    for s in input_str:
        if s == "Z":
            out_str += "A"
        else:
            out_str += chr(ord(s) + 1)
    answers.append(out_str)

for index, answer in enumerate(answers):
    print(f"String #{index + 1}")
    print(answer)
    if index != case - 1:
        print()
