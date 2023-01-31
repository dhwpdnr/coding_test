def solution(order):
    answer = 0
    num = str(order)
    for i in num:
        if i in ["3", "6", "9"]:
            answer += 1
    return answer

    # 프로그래머스 연습문제 369 게임
