from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    doc = [0 for i in range(len(priorities))]
    doc[location] = 1
    doc = deque(doc)
    while (doc):
        a = q.popleft()
        b = doc.popleft()
        if len(q) > 1 and max(q) > a:
            q.append(a)
            doc.append(b)
        else:
            answer += 1
            if b == 1:
                break
    return answer

    # 프로그래머스 스택/큐 프린터