case = int(input())

stack = []
answer = []

for _ in range(case):
    command = list(map(str, input().split()))

    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack.pop())
    elif command[0] == "size":
        answer.append(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif command[0] == "top":
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack[-1])

for i in answer:
    print(i)
