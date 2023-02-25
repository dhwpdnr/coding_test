def solution(s):
    answer = ''
    s_list = s.split(' ')
    for i in s_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]

    # 프로그래머스 연습문제 이상한 문자 만들기