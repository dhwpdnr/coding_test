# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 만들기 6
# https://school.programmers.co.kr/learn/courses/30/lessons/181859?language=python3
def solution(arr):
    answer = []
    i = 0
    for a in arr:
        if answer == []:
            answer.append(a)
        elif answer[-1] == a:
            answer.pop()
        else:
            answer.append(a)

        i += 1
    return answer if answer else [-1]


q = solution([0, 1, 1, 1, 0])
assert q == [0, 1, 0]
print(q)

q = solution([0, 1, 0, 1, 0])
assert q == [0, 1, 0, 1, 0]
print(q)

q = solution([0, 1, 1, 0])
assert q == [-1]
print(q)
