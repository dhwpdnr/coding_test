# 프로그래머스
# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    answer = 0
    for _ in range(3 * len(queue1)):
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer += 1
    return -1


q = solution([3, 2, 7, 2], [4, 6, 5, 1])
assert q == 2
print(q)

q = solution([1, 2, 1, 2], [1, 10, 1, 2])
assert q == 7
print(q)

q = solution([1, 1], [1, 5])
assert q == -1
print(q)
