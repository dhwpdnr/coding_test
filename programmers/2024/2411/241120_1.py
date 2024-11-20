# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > qr code
# https://school.programmers.co.kr/learn/courses/30/lessons/181903
def solution(q, r, code):
    answer = ''
    for i in code[r::q]:
        answer += i
    return answer


q = solution(3, 1, "qjnwezgrpirldywt")
assert q == "jerry"
print(q)

q = solution(1, 0, "programmers")
assert q == "programmers"
print(q)
