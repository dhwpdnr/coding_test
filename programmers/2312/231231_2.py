# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt = 0
    zero_count = 0
    while True:
        if s == "1":
            break;
        zero_count += s.count("0")
        s = s.replace("0", '')
        s = bin(len(s))[2:]
        cnt += 1

    return [cnt, zero_count]


q = solution("110010101001")
assert q == [3, 8]
print(q)

q = solution("01110")
assert q == [3, 3]
print(q)

q = solution("1111111")
assert q == [4, 1]
print(q)
