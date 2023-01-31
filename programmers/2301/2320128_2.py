def solution(num, k):
    num_list = list(str(num))
    i = 0
    while i < len(num_list):
        if k == int(num_list[i]):
            return i + 1
        i += 1
    return -1

    # 프로그래머스 연습문제 숫자 찾기
