def solution(n):
    if n % 2 == 0:
        return "수박" * (n // 2)
    else:
        return "수박" * (n // 2) + "수"

    # 프로그래머스 연습문제 수박수박수박