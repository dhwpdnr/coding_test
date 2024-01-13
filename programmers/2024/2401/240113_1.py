# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    next = n
    answer = 0
    while True:
        next += 1
        if bin(n)[2:].count('1') == bin(next)[2:].count('1'):
            answer = next
            break

    return answer


q = solution(78)
assert q == 83
print(q)

q = solution(15)
assert q == 23
print(q)
