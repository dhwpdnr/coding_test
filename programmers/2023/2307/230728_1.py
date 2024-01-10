# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 카드 뭉치
# https://school.programmers.co.kr/learn/courses/30/lessons/159994
from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for i in goal:
        if cards1 and cards1[0] == i:
            cards1.popleft()
        elif cards2 and cards2[0] == i:
            cards2.popleft()
        else:
            return "No"
    return "Yes"


q = solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
assert q == "Yes", "불일치"
print(q)

q = solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])
assert q == "No", "불일치"
print(q)
