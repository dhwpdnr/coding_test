from collections import deque

case = int(input())

que = deque()
answer = []

for _ in range(case):
    command = list(map(str, input().split()))

    if command[0] == "push":
        que.append(command[1])
    elif command[0] == "pop":
        if len(que) == 0:
            answer.append(-1)
        else:
            answer.append(que.popleft())
    elif command[0] == "size":
        answer.append(len(que))
    elif command[0] == "empty":
        if len(que) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif command[0] == "front":
        if len(que) == 0:
            answer.append(-1)
        else:
            answer.append(que[0])
    elif command[0] == "back":
        if len(que) == 0:
            answer.append(-1)
        else:
            answer.append(que[-1])

for i in answer:
    print(i)
