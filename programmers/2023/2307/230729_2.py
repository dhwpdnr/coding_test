# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > n보다 커질 때까지 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181884

def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            return answer


q = solution([34, 5, 71, 29, 100, 34], 123)
assert q == 139, "불일치"
print(q)

q = solution([58, 44, 27, 10, 100], 139)
assert q == 239, "불일치"
print(q)
