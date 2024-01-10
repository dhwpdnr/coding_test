def solution(A, B):
    if A == B:
        return 0
    for i in range(len(A)):
        a = A[-1]
        A = a + A[:-1]
        if A == B:
            return i + 1
    return -1

    # 프로그래머스 연습문제 문자열 밀기