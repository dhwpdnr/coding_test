# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/159994
def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for alphabet in target:
            arr = []
            for key in keymap:
                if alphabet in key:
                    arr.append(key.index(alphabet))
            if not arr == []:
                count += min(arr) + 1
            else:
                count = 0
                break
        if count == 0:
            answer.append(-1)
        else:
            answer.append(count)
    return answer


# 다른 사람 풀이
def solution(keymap, targets):
    answer = []
    for target in targets:
        temp = 0
        for s in target:
            touch = [i.index(s) + 1 for i in keymap if s in i]
            if len(touch) == 0:
                answer.append(-1)
                break
            else:
                touch = min(touch)
                temp += touch
        if touch:
            answer.append(temp)
    return answer


q = solution(["ABACD", "BCEFD"], ["ABCD", "AABB"])
assert q == [9, 4], "불일치"
print(q)

q = solution(["AA"], ["B"])
assert q == [-1], "불일치"
print(q)

q = solution(["AGZ", "BSSS"], ["ASA", "BGZ"])
assert q == [4, 6], "불일치"
print(q)
