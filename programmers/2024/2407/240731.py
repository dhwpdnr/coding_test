# 프로그래머스
# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# BFS 풀이
def solution(numbers, target):
    sums = [0]
    for number in numbers:
        temp = []
        for a in sums:
            temp.append(a + number)
            temp.append(a - number)
        sums = temp

    return sums.count(target)


# DFS 풀이
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


from itertools import product


# 데카르트 곱 풀이
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


q = solution([1, 1, 1, 1, 1], 3)
assert q == 5
print(q)

q = solution([4, 1, 2, 1], 4)
assert q == 2
print(q)
