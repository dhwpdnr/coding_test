def solution(arr1, arr2):
    answer = []
    for i, k in zip(arr1, arr2):
        sum_list = []
        for n, t in zip(i, k):
            sum_list.append(n + t)
        answer.append(sum_list)
    return answer

    # 프로그래머스 연습문제 행렬의 덧


def solution(arr1, arr2):
    return [[a + b for a, b in zip(i, k)] for i, k in zip(arr1, arr2)]

    # 리스트 컴프리헨션 사용
