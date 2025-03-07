# 프로그래머스
# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    result = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0
    }
    for s, c in zip(survey, choices):
        if c > 4:
            result[s[1]] += c - 4
        elif c < 4:
            result[s[0]] += 4 - c

    li = list(result.items())

    for i in range(0, 8, 2):
        if li[i][1] < li[i + 1][1]:
            answer += li[i + 1][0]
        else:
            answer += li[i][0]

    return answer


q = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
assert q == "TCMA"
print(q)

q = solution(["TR", "RT", "TR"], [7, 1, 3])
assert q == "RCJA"
print(q)
