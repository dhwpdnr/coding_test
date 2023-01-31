def solution(operations):
    answer = []
    que = []
    for op in operations:
        if op[0] == "I":
            que.append(op[2:])
            que = list(map(int, que))
            que.sort()
        elif op[0] == "D" and op[2] == "1":
            if len(que) != 0:
                que.pop()
        elif op[0] == "D" and op[2] == "-":
            if len(que) != 0:
                que.pop(0)
    l = len(que)
    if l != 0:
        answer.append(que[l - 1])
        answer.append(que[0])
    else:
        answer = [0, 0]
    return answer

    # 프로그래머스 힙 이중우선순위 큐