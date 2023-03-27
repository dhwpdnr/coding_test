n = str(input())
answer = ""

for i in n:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()

print(answer)
