# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    yearn_dict = {}
    for n, y in zip(name, yearning):
        yearn_dict[n] = y
    for p in photo:
        score = 0
        for i in p:
            try:
                score += yearn_dict[i]
            except:
                pass
        answer.append(score)
    return answer


# 다른 사람의 풀이
# def solution(이름, 점수, 사진):
#     return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]


q = solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
             [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
assert q == [19, 15, 6], "불일치"
print(q)

q = solution(["kali", "mari", "don"], [11, 1, 55],
             [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
assert q == [67, 0, 55], "불일치"
print(q)

q = solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"], ["kein", "deny", "may"], ["kon", "coni"]])
assert q == [5, 15, 0], "불일치"
print(q)
