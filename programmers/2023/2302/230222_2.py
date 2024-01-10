def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False
    return answer

    # 프로그래머스 연습문제 문자열 다루기 기본


def solution(s):
    return s.isdigit() and len(s) in [4, 6]

    # 더 간단한 풀이
