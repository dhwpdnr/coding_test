# 프로그래머스
# 코딩테스트 연습 > 완전탐색 > 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []

    yellow_x = 0
    yellow_y = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_x = int(yellow / i)
            yellow_y = i
            if yellow_x * 2 + yellow_y * 2 + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)

                return sorted(answer, reverse=True)

    return answer


q = solution(10, 2)
assert q == [4, 3]
print(q)

q = solution(8, 1)
assert q == [3, 3]
print(q)

q = solution(24, 24)
assert q == [8, 6]
print(q)
