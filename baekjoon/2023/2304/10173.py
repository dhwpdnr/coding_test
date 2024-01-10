answers = []
while True:
    sentence = str(input())
    if sentence == "EOI":
        break
    else:
        sentence = sentence.lower()
        if "nemo" in sentence:
            answers.append("Found")
        else:
            answers.append("Missing")

for answer in answers:
    print(answer)
