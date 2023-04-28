sentence = str(input())

case = int(input())

answer = 0

for _ in range(case):
    ring = str(input())
    if sentence in ring * 2:
        answer += 1

print(answer)
