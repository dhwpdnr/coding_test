case = int(input())
answers = []

for _ in range(case):
    arr = input()
    stack = []
    for i in arr:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                answers.append("NO")
                break
    else:
        if stack:
            answers.append("NO")
        else:
            answers.append("YES")

for answer in answers:
    print(answer)
