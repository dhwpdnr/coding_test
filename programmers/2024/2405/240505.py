# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/181923
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 수열과 구간 쿼리 2


def solution(arr, queries):
    answer = []
    for query in queries:
        temp = []
        for i in range(query[0], query[1] + 1):
            if arr[i] > query[2]:
                temp.append(arr[i])
        try:
            answer.append(min(temp))
        except:
            answer.append(-1)
    return answer


q = solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]])
assert q == [3, 4, -1]
print(q)
