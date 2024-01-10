from itertools import combinations


def is_prime_number(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for i in combi:
        if is_prime_number(sum(i)):
            answer += 1
    return answer


    # 프로그래머스 연습문제 소수 만들기
