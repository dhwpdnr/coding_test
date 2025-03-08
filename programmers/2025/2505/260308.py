# 프로그래머스
# 코딩테스트 연습 > 완전탐색 > 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product


# 전체 경우의 수 생성 후 정렬하여 인덱스 반환
def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for per in product(li, repeat=i):
            answer.append(''.join(per))
    answer.sort()
    return answer.index(word) + 1


# DFS로 모든 경우의 수 생성 후 인덱스 반환
def solution(word):
    word_list = []
    words = 'AEIOU'

    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
            word_list.append(w + words[i])
            dfs(cnt + 1, w + words[i])

    dfs(0, "")

    return word_list.index(word) + 1


# 수학적으로 계산
def solution(word):
    answer = 0
    dic = ['A', 'E', 'I', 'O', 'U']
    li = [5 ** i for i in range(len(dic))]

    for i in range(len(word) - 1, -1, -1):
        idx = dic.index(word[i])
        for j in range(5 - i):
            answer += li[j] * idx
        answer += 1
    return answer


q = solution("AAAAE")
assert q == 6
print(q)

q = solution("AAAE")
assert q == 10
print(q)

q = solution("I")
assert q == 1563
print(q)

q = solution("EIO")
assert q == 1189
print(q)
