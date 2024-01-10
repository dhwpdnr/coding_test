def solution(M, N):
    answer = 0
    if M == 1:
        return N - 1
    elif N == 1:
        return M - 1
    elif M == 1 and N == 1:
        return 0
    else:
        return (M - 1) + (M * (N - 1))

    # 프로그래머스 연습문제 종이자르기
