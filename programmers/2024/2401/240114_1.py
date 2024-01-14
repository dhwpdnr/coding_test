# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 피보나치 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)

    return answer[-1]


q = solution(3)
assert q == 2
print(q)

q = solution(5)
assert q == 5
print(q)
