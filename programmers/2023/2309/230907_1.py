# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 꼬리 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181841

def solution(str_list, ex):
    return "".join(["" if ex in i else i for i in str_list])


q = solution(["abc", "def", "ghi"], "ef")
assert q == "abcghi"
print(q)

q = solution(["abc", "bbc", "cbc"], "c")
assert q == ""
print(q)
