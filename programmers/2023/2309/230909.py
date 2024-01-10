# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 조각하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        if i % 2 == 0:
            answer = answer[:query[i] + 1]
        else:
            answer = answer[query[i]:]
    return answer


q = solution([0, 1, 2, 3, 4, 5], [4, 1, 2])
assert q == [1, 2, 3]
print(1)
