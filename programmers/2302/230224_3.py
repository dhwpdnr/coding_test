def solution(n):
    answer = ''
    while n >= 1:
        n, rest = divmod(n, 3)
        answer += str(rest)

    return int(answer, 3)

    # 프로그래머스 연습문제 3진법 뒤집기
