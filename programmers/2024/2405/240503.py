# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/181890
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 왼쪽 오른쪽

def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i + 1:]
    return []


q = solution(["u", "u", "l", "r"])
assert q == ["u", "u"]
print(q)

q = solution(["l"])
assert q == []
print(q)
