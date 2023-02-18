def solution(arr, divisor):
    answer = ([i for i in arr if i % divisor == 0]) or [-1]
    answer.sort()
    return answer

    # 프로그래머스 연습문제 나누어 떨어지는 숫자 배열