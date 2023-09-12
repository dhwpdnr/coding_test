# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 코드 처리하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181932

def solution(code):
    mode = True
    ret = ''
    for index, value in enumerate(code):
        if mode:
            if value != '1' and index % 2 == 0:
                ret += value
            elif value == '1':
                mode = False
        else:
            if value != '1' and index % 2 != 0:
                ret += value
            elif value == '1':
                mode = True
    return 'EMPTY' if len(ret) == 0 else ret


q = solution("abc1abc1abc")
assert q == "acbac"
print(q)
