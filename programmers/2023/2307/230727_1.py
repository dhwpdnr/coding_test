# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 세 개의 구분자
# https://school.programmers.co.kr/learn/courses/30/lessons/181862

def solution(myStr):
    answer = []
    myStr = myStr.replace("a", " ")
    myStr = myStr.replace("b", " ")
    myStr = myStr.replace("c", " ")
    arr = myStr.split(" ")
    for i in arr:
        if i != "":
            answer.append(i)
    if answer == []:
        return ["EMPTY"]
    return answer


# 다른 사람의 풀이
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']


q = solution("baconlettucetomato")
assert q == ["onlettu", "etom", "to"], "불일치"
print(q)

q = solution("abcd")
assert q == ["d"], "불일치"
print(q)

q = solution("cabab")
assert q == ["EMPTY"], "불일치"
print(q)
