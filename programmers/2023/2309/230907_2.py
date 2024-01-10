# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    isx, isnotx = 0, 0
    for i in s:
        if isx == isnotx:
            answer += 1
            x = i
            isx, isnotx = 0, 0

        if i == x:
            isx += 1
        else:
            isnotx += 1

    return answer


q = solution("banana")
assert q == 3
print(q)

q = solution("abracadabra")
assert q == 6
print(q)

q = solution("aaabbaccccabba")
assert q == 3
print(q)
