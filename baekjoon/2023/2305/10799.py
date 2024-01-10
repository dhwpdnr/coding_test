case = input()

answer = 0

stack = []

for i in range(len(case)):
    if case[i] == "(":
        stack.append("(")
    else:
        if case[i - 1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
