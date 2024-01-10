def solution(n):
    answer = sorted(list(str(n)), reverse=True)
    num = ""
    for i in answer:
        num += i
    return int(num)

    # 프로그래머스 연습문제 정수 내림차순으로 배치하기


def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int("".join(ls))

    # join 사용한 간단한 풀이
