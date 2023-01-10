def solution(numbers, k):
    answer = numbers[2 * (k - 1) % len(numbers)]
    return answer

    # 프로그래머스 연습 문제