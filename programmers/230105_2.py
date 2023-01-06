def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(int(i)+97)
    return answer

    # 프로그래머스 연습문제