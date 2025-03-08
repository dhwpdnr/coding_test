# 프로그래머스
# 코딩테스트 연습 > 완전탐색 > 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for need, spend in p:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        answer = max(answer, cnt)
    return answer


q = solution(80, [[80, 20], [50, 40], [30, 10]])
assert q == 3
print(q)
