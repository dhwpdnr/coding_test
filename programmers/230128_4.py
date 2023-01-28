def solution(n):
    nlist = list(str(n))
    answer = 0
    for i in nlist:
        answer += int(i)
    return answer

    # 프로그래머스 연습문제 자릿수 더하기