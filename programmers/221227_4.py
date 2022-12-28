def solution(array):
    from collections import Counter
    c = Counter(array)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    if len(modes) == 1 : return modes[0]
    else : return -1

    # 프로그래머스 코딩테스트 입문