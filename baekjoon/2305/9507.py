case = int(input())
answers = []
for i in range(case):
    arr = [1, 1, 2, 4]
    n = int(input())
    for j in range(4, n + 1):
        arr.append(arr[j - 1] + arr[j - 2] + arr[j - 3] + arr[j - 4])
    answers.append(arr[n])

for answer in answers:
    print(answer)
