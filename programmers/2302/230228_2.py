def solution(sizes):
    row = 0
    col = 0
    for i in sizes:
        i.sort()
        if i[0] > row:
            row = i[0]
        if i[1] > col:
            col = i[1]
    return row * col

    # 프로그래머스 연습문제 최소직사각형
