# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    return "".join([arr[(arr.index(i) + index) % len(arr)] for i in s])


#다른 사람의 풀이
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result



q = solution("aukks", "wbqd", 5)
assert q == "happy", "불일치"
print(q)
