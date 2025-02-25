# 프로그래머스
# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3


def solution(board, moves):
    bucket = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                bucket.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop()
                        bucket.pop()
                        answer += 2
                break
    return answer


q = solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
             [1, 5, 3, 5, 1, 2, 1, 4])
assert q == 4
print(q)
