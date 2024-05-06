# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/181837
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 커피 심부름


def solution(order):
    answer = 0
    for coffee in order:
        if "cafelatte" in coffee:
            answer += 5000
        else:
            answer += 4500
    return answer


q = solution(["cafelatte", "americanoice", "hotcafelatte", "anything"])
assert q == 19000
print(q)

q = solution(["americanoice", "americano", "iceamericano"])
assert q == 13500
print(q)
