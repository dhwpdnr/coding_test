def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x: x[n])

    # 프로그래머스 연습문제 문자열 내 마음대로 정렬하기