# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌3 > n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

# 시간 초과
def solution(n, left, right):
    answer = []

    for i in range(n):
        for j in range(n):
            answer.append(max(i + 1, j + 1))

    return answer[left:right + 1]


def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer


q = solution(3, 2, 5)
assert q == [3, 2, 2, 3]
print(q)

q = solution(4, 7, 14)
assert q == [4, 3, 3, 3, 4, 4, 4, 4]
print(q)
