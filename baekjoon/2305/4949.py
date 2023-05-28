answers = []

while True:
    input_str = input()
    if input_str == ".":
        break
    else:
        stack = []
        for i in input_str:
            if i == "(":
                stack.append("(")
            elif i == "[":
                stack.append("[")
            elif i == ")":
                if stack == [] or stack[-1] != "(":
                    answers.append("no")
                    break
                else:
                    stack.pop()
            elif i == "]":
                if stack == [] or stack[-1] != "[":
                    answers.append("no")
                    break
                else:
                    stack.pop()
        else:
            if stack:
                answers.append("no")
            else:
                answers.append("yes")

for answer in answers:
    print(answer)
