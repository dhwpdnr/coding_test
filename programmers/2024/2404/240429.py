# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 코딩테스트 연습 > 정렬 > H-Index


def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        h_index = n - i
        if citations[i] >= h_index:
            return h_index
    return 0


q = solution([3, 0, 6, 1, 5])
assert q == 3
print(q)
