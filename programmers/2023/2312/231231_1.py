# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


q = solution([1, 4, 2], [5, 4, 4])
assert q == 29
print(q)

q = solution([1, 2], [3, 4])
assert q == 10
print(q)
