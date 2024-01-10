def solution(keyinput, board):
    x = board[0] // 2
    y = board[1] // 2
    answer = [0, 0]
    for i in keyinput:
        if i == "left":
            if answer[0] == -x:
                pass
            else:
                answer[0] -= 1
        elif i == "right":
            if answer[0] == x:
                pass
            else:
                answer[0] += 1
        elif i == "up":
            if answer[1] == y:
                pass
            else:
                answer[1] += 1
        elif i == "down":
            if answer[1] == -y:
                pass
            else:
                answer[1] -= 1

    return answer

    # 프로그래머스 연습문제 캐릭터의 좌표
