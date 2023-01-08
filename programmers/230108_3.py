def solution(num_list, n):
    answer = []
    k = 0
    i = 0
    while k < len(num_list):
        if (k+1) % n == 1 :
            answer.append([])
        answer[i].append(num_list[k])
        if (k+1) % n == 0 :
            i += 1
        k += 1
    return answer

    # 프로그래머스 연습 문제