def solution(n):
    answer = []
    result = []
    num = n
    s = 2
    while s <= num:
        if num % s == 0:
            answer.append(s)
            num = num // s
        else:
            s = s + 1
    for i in answer:
        if i not in result:
            result.append(i)
    return result

    #프로그래머스 연습문제 소인수 분해