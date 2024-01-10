def solution(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        return numbers[0] * numbers[1]
    else:
        return numbers[-1] * numbers[-2]

    # 프로그래머스 연습문제 최댓값 만들기 (2)


def another(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

    # if문이 아닌 max를 사용해도 가능하다
