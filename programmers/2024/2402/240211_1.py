# 프로그래머스
# 코딩테스트 연습 > PCCE 기출문제 > [PCCE 기출문제] 9번 / 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    n = len(board)
    answer = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            if board[h][w] == board[h_check][w_check]:
                answer += 1
    return answer


q = solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"],
              ["orange", "orange", "red", "blue"]], 1, 1)
assert q == 2
print(q)

q = solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1)
assert q == 1
print(q)
