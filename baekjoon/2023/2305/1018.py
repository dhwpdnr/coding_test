col, row = map(int, input().split())
board = []

black = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"]
]

white = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"]
]

for _ in range(col):
    board.append(list(input()))

answer = []

for col_index in range(col - 7):
    for row_index in range(row - 7):
        white_paint = 0
        black_paint = 0
        for i in range(8):
            for t in range(8):
                if board[i + col_index][t + row_index] != white[i][t]:
                    white_paint += 1
                if board[i + col_index][t + row_index] != black[i][t]:
                    black_paint += 1
        answer.append(white_paint)
        answer.append(black_paint)

print(min(answer))
