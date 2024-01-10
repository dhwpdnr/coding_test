def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i.replace("=", "==")):
            answer.append('O')
        else:
            answer.append("X")
    return answer

    # 프로그래머스 연습문제 OX퀴즈