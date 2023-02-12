def solution(n):
    answer = 0
    number = n
    while True:
        answer += number % 10
        number = number // 10
        if number == 0:
            break
    return answer

    # 프로그래머스 연습문제 자릿수 더하기