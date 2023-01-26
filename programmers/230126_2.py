def solution(array):
    answer = []
    for index, num in enumerate(array):
        if index == 0:
            answer.append(num)
            answer.append(index)
        elif num > answer[0]:
            answer = []
            answer.append(num)
            answer.append(index)
    return answer

    # 프로그래머스 연습문제 가장 큰 수 찾기
