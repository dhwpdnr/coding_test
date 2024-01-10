arr = [input() for _ in range(5)]

answer = []

for index, item in enumerate(arr):
    if "FBI" in item:
        answer.append(index + 1)

if len(answer) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(map(str, answer)))
