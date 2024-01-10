# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 옹알이 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    repeats = ["ayaaya", "yeye", "woowoo", "mama"]

    for x in babbling:
        for word in repeats:
            x = x.replace(word, "X")
        for word in words:
            x = x.replace(word, "O")

        isValid = True
        for char in x:
            if char != "O":
                isValid = False
                break
        if isValid == True:
            answer += 1

    return answer


q = solution(["aya", "yee", "u", "maa"])
assert q == 1
print(q)

q = solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
assert q == 2
print(q)
