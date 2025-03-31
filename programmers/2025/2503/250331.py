# 프로그래머스
# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334
from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))

    user = defaultdict(set)

    report_cnt = defaultdict(int)

    for r in report:
        a, b = r.split()
        user[a].add(b)
        report_cnt[b] += 1

    for i in id_list:
        result = 0
        for u in user[i]:
            if report_cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer


q = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2)
assert q == [2, 1, 1, 0]
print(q)

q = solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
assert q == [0, 0]
print(q)
