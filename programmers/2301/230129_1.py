def solution(str1, str2):
    len_str2 = len(str2)
    i = 0
    arr = []
    while i < len(str1) - len_str2 + 1:
        arr.append(str1[i:i + len_str2])
        i += 1
    if str2 in arr:
        return 1
    else:
        return 2

    # 프로그래머스 연습문제 문자열 안에 문자열