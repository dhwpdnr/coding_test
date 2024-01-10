def solution(numbers):
    numbers.sort()
    l = len(numbers)
    answer = numbers[l-1] * numbers[l-2]
    return answer

    # 프로그래머스 최대값 만들기 (1)