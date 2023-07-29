# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 첫 번째로 나오는 음수
# https://school.programmers.co.kr/learn/courses/30/lessons/181896

def solution(num_list):
    for i, v in enumerate(num_list):
        if v < 0:
            return i
    return -1


q = solution([12, 4, 15, 46, 38, -2, 15])
assert q == 5, "불일치"
print(q)

q = solution([13, 22, 53, 24, 15, 6])
assert q == -1, "불일치"
print(q)
