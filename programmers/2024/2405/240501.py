# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/181913
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 문자열 여러 번 뒤집기

def solution(my_string, queries):
    for start, end in queries:
        my_string = my_string[:start] + my_string[start:end + 1][::-1] + my_string[end + 1:]
    return my_string


q = solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])
assert q == "programmers"
print(q)
