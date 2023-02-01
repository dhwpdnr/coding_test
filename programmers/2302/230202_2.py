def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

    # 프로그래머스 연습문제 저주의 숫자 3
