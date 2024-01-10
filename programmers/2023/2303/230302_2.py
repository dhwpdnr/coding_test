def solution(array, commands):
    answer = []
    for i in commands:
        arr = array[i[0] - 1:i[1]]
        arr.sort()
        answer.append(arr[i[2] - 1])
    return answer

    # 프로그래머스 연습문제 K번째 수
