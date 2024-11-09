# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265?language=python3
from collections import Counter


def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    answer = 0
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1
    return answer


q = solution([1, 2, 1, 3, 1, 4, 1, 2])
assert q == 2
print(q)

q = solution([1, 2, 3, 1, 4])
assert q == 0
print(q)
