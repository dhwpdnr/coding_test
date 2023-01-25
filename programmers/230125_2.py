from collections import Counter


def solution(s):
    count = Counter(s)
    ls = []
    for key, value in count.items():
        if value == 1:
            ls.append(key)
    ls.sort()
    answer = ""
    for i in ls:
        answer += i
    return answer

    # 프로그래머스 연습문제 한 번만 등장한 문자

