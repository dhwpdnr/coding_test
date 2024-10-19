# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] n진수 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

    return rev_base[::-1]


def solution(n, t, m, p):
    answer = ""
    test = ""
    for i in range(m * t):
        test += str(convert(i, n))

    while len(answer) < t:
        answer += test[p - 1]
        p += m

    return answer


q = solution(2, 4, 2, 1)
assert q == "0111"
print(q)

q = solution(16, 16, 2, 1)
assert q == "02468ACE11111111"
print(q)

q = solution(16, 16, 2, 2)
assert q == "13579BDF01234567"
print(q)
