# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 주사위 게임 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181916

from collections import Counter


def solution(a, b, c, d):
    answer = 0
    cnt = Counter([a, b, c, d]).most_common(4)
    len_cnt = len(cnt)

    if len_cnt == 1:
        answer = 1111 * int(cnt[0][0])
    if len_cnt == 2:
        if cnt[0][1] == 2:
            answer = (cnt[0][0] + cnt[1][0]) * abs(cnt[0][0] - cnt[1][0])
        else:
            answer = pow((10 * cnt[0][0] + cnt[1][0]), 2)
    if len_cnt == 3:
        answer = cnt[1][0] * cnt[2][0]
    if len_cnt == 4:
        answer = min(a, b, c, d)

    return answer


q = solution(2, 2, 2, 2)
assert q == 2222
print(q)

q = solution(4, 1, 4, 4)
assert q == 1681
print(q)

q = solution(6, 3, 3, 6)
assert q == 27
print(q)

q = solution(2, 5, 2, 6)
assert q == 30
print(q)

q = solution(6, 4, 2, 5)
assert q == 2
print(q)
