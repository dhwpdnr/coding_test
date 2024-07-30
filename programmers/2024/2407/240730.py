# 프로그래머스
# 코딩테스트 연습 > 힙(Heap) > 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# heapq 풀이
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mix = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, mix)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer


# deque 풀이
# heap 을 사용한 풀이보다 deque 를 사용한 풀이가 더 빠르다.
from collections import deque


def solution(scoville, K):
    answer = 0
    scoville.sort()
    q = deque(scoville)
    mix_q = deque()

    while (q and q[0] < K) or (mix_q and mix_q[0] < K):
        answer += 1
        if len(q) + len(mix_q) <= 1:
            return -1
        food = [0] * 2
        for a in range(2):
            if q and mix_q:
                if q[0] < mix_q[0]:
                    food[a] = q.popleft()
                else:
                    food[a] = mix_q.popleft()
            elif q:
                food[a] = q.popleft()
            else:
                food[a] = mix_q.popleft()

        mix_q.append(food[0] + food[1] * 2)

    return answer


q = solution([1, 2, 3, 9, 10, 12], 7)
assert q == 2
print(q)
