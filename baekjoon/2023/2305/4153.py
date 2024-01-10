answers = []
while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    else:
        arr.sort()
        if arr[2] ** 2 == arr[0] ** 2 + arr[1] ** 2:
            answers.append("right")
        else:
            answers.append("wrong")

for answer in answers:
    print(answer)
