# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/181830
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 정사각형으로 만들기

def solution(arr):
    answer = []
    row = len(arr)
    col = len(arr[0])

    if row > col:
        for i in arr:
            answer.append(i + [0] * (row - col))
    elif row < col:
        for _ in range(col - row):
            arr.append([0] * col)
        answer = arr
    else:
        answer = arr
    return answer


q = solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]])
assert q == [[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]]
print(q)

q = solution([[57, 192, 534, 2], [9, 345, 192, 999]])
assert q == [[57, 192, 534, 2], [9, 345, 192, 999], [0, 0, 0, 0], [0, 0, 0, 0]]
print(q)

q = solution([[1, 2], [3, 4]])
assert q == [[1, 2], [3, 4]]
print(q)
