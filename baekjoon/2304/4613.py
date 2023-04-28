arr = []

while True:
    s = str(input())

    if s == "#":
        break
    else:
        answer = 0
        for index, i in enumerate(s):
            if i == " ":
                pass
            else:
                answer += (ord(i) - 64) * (index + 1)
        arr.append(answer)

for k in arr:
    print(k)
