def solution(emergency):
    answer = []
    arr = sorted(emergency)
    arr2 = arr[::-1]
    for i in emergency :
        index = arr2.index(i)
        answer.append(index+1)
    return answer

    # 프로그래머스 연습문제