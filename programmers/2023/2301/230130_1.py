def solution(array):
    answer = 0
    for i in array:
        for k in list(str(i)):
            if k == '7':
                answer += 1
    return answer

    # 프로그래머스 연습문제 7의 개수