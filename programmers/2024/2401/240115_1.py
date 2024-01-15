# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 행렬의 곱셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12949


def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


# zip, sum, 리스트 컴프리핸션 사용 풀이
def productMatrix(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


q = solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
assert q == [[15, 15], [15, 15], [15, 15]]
print(q)

q = solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
assert q == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
print(q)
