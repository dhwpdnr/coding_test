from collections import deque

case = int(input())

deq = deque()
answer = []

for _ in range(case):
    command = list(map(str, input().split()))

    if command[0] == "push_front":
        deq.appendleft(command[1])
    elif command[0] == "push_back":
        deq.append(command[1])
    elif command[0] == "pop_front":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq.popleft())
    elif command[0] == "pop_back":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq.pop())
    elif command[0] == "size":
        answer.append(len(deq))
    elif command[0] == "empty":
        if len(deq) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif command[0] == "front":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq[0])
    elif command[0] == "back":
        if len(deq) == 0:
            answer.append(-1)
        else:
            answer.append(deq[-1])

for i in answer:
    print(i)
