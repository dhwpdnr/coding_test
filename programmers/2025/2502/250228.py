# 프로그래머스
# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for word in new_id:
        if word.isalnum() or word in ["-", "_", "."]:
            answer += word

    while ".." in answer:
        answer = answer.replace("..", ".")

    if answer[0] == "." and len(answer) > 1:
        answer = answer[1:]

    if answer[-1] == ".":
        answer = answer[:-1]

    if answer == "":
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer


q = solution("...!@BaT#*..y.abcdefghijklm")
assert q == "bat.y.abcdefghi"
print(q)

q = solution("z-+.^.")
assert q == "z--"
print(q)

q = solution("=.=")
assert q == "aaa"
print(q)

q = solution("123_.def")
assert q == "123_.def"
print(q)

q = solution("abcdefghijklmn.p")
assert q == "abcdefghijklmn"
print(q)
