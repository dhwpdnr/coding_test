# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 만들기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
    if answer == []:
        return [-1]
    return answer


q = solution(5, 555)
assert q == [5, 50, 55, 500, 505, 550, 555]
print(q)

q = solution(10, 20)
assert q == [-1]
print(q)
