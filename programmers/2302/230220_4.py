def solution(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2 - 1: len(s) // 2 + 1]

    # 프로그래머스 연습문제 가운데 글자 가져오기