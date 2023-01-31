from collections import deque
def solution(people, limit):
    boat = 0
    q = deque(sorted(people))
    while len(q) > 1:
        if q[0] + q[-1] <= limit :
            q.pop()
            q.popleft()
            boat += 1
        else :
            q.pop()
            boat += 1
    if len(q) == 1:
        boat += 1
    return boat

    # 프로그래머스 구명보트