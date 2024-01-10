def solution(arr):
    sort_arr = sorted(arr)
    arr.remove(sort_arr[0])
    if arr == []:
        return [-1]
    return arr

    # 프로그래머스 연습문제 제일 작은 수 제거하기


def solution(arr):
    return [i for i in arr if i > min(arr)] or [-1]

    # 리스트 컴프리헨션 사용으로 간단하게 구현
