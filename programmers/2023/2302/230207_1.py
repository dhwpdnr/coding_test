def solution(elements):
    ls = []
    elements_len = len(elements)
    elements = elements * 2
    for i in range(elements_len):
        for k in range(elements_len):
            ls.append(sum(elements[k:i + k + 1]))
    ls = set(ls)
    return len(ls)

    # 프로그래머스 연습문제 연속 부분 수열 합의 개수