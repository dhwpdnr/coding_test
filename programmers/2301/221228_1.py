def solution(n, words):
    array = []
    answer = []
    i=0
    while i < len(words) :
        if array == [] :
            array.append(words[i])
        elif words[i] in array :
            answer.append((i%n)+1)
            answer.append(int((i+n)/n))
            break
        elif array[-1][-1] == words[i][0] :
            array.append(words[i])
        elif array[-1][-1] != words[i][0] :
            answer.append((i%n)+1)
            answer.append(int((i+n)/n))
            break
        i += 1
    if answer == [] :
        answer = [0,0]
    return answer


    #프로그래머스 영어 끝말잇기