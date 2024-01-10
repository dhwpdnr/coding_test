def solution(k, score):
    answer = []
    arr = []
    for i in score:
        if len(arr) < k:
            arr.append(i)
            arr.sort()
            answer.append(arr[0])
        else:
            if arr[0] < i:
                arr.pop(0)
                arr.append(i)
                arr.sort()
                answer.append(arr[0])
            else:
                answer.append(arr[0])
    return answer

    # 프로그래머스 연습문제 명예의 전당(1)
