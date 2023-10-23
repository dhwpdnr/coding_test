# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 무작위로 K개의 수 뽑기
# https://school.programmers.co.kr/learn/courses/30/lessons/181858

def solution(arr, k):
    answer = []
    for i in arr:
        if not i in answer:
            answer.append(i)
    if len(answer) >= k:
        return answer[:k]
    else:
        for i in range(k - len(answer)):
            answer.append(-1)
        return answer


q = solution([0, 1, 1, 2, 2, 3], 3)
assert q == [0, 1, 2]
print(q)

q = solution([0, 1, 1, 1, 1], 4)
assert q == [0, 1, -1, -1]
print(q)
