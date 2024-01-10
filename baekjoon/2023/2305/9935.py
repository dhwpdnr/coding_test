# 시간 초과

sentence = str(input())
bomb = str(input())
sentence_cp = sentence

while True:
    sentence = sentence_cp
    sentence_cp = sentence.replace(bomb, "")
    if sentence_cp == sentence:
        break

if sentence_cp == "":
    print("FRULA")
else:
    print(sentence_cp)


# 개선 코드

S = str(input())
explosion_string = str(input())

stack = []
ex_len = len(explosion_string)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-ex_len:]) == explosion_string:
        for _ in range(ex_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')