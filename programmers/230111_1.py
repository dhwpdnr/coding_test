def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic.keys():
            dic[i[1]].append(i[0])
        else :
            dic[i[1]] = [i[0]]
    for value in dic.values():
        answer *= (len(value)+1)
    return answer-1

    # 프로그래머스 해시 위장