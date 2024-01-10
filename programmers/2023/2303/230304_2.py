def solution(s):
    answer = []
    s_dic = {}
    count = 1
    for i in s:
        if i in s_dic:
            answer.append(count - s_dic[i])
            s_dic[i] = count
        else:
            answer.append(-1)
            s_dic[i] = count
        count += 1
    return answer


    # 프로그래머스 연습문제 가장 가까운 같은 글자