answer = []
while True:
    try:
        sentence = str(input())
        answer.append(sentence)
    except:
        break
for i in answer:
    print(i)
