def solution(before, after):
    b = sorted(list(before))
    a = sorted(list(after))
    if a == b:
        return 1
    else:
        return 0

    # 프로그래머스 연습문제 A로 B 만들기


def another(before, after):
    b = sorted(before)
    a = sorted(after)
    if a == b:
        return 1
    else:
        return 0

    # 문자열도 sorted 가능