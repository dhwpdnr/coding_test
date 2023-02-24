def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        elif i != answer[-1]:
            answer.append(i)
    return answer

    # 프로그래머스 연습문제 같은 숫자는 싫어
