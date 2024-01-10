answer = []
while True:
    try:
        sentence = str(input())
        total = [0, 0, 0, 0]
        for i in sentence:
            if i.islower():
                total[0] += 1
            elif i.isupper():
                total[1] += 1
            elif i.isdigit():
                total[2] += 1
            elif i == " ":
                total[3] += 1
        answer.append(total)
    except:
        break

for k in answer:
    print(k[0], k[1], k[2], k[3])
