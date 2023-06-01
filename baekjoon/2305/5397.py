case = int(input())
answers = []

for _ in range(case):
    stack_l = []
    stack_r = []
    commands = str(input())
    for command in commands:
        if command == "<":
            if stack_l:
                stack_r.append(stack_l.pop())
        elif command == ">":
            if stack_r:
                stack_l.append(stack_r.pop())
        elif command == "-":
            if stack_l:
                stack_l.pop()
        else:
            stack_l.append(command)
    answers.append("".join(stack_l + list(reversed(stack_r))))

for answer in answers:
    print(answer)
