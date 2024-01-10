# 프로그래머스
# 코딩테스트 연습 > 연습문제 > JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    arr = s.split(' ')
    answer = []
    for i in arr:
        answer.append(i.capitalize())
    return ' '.join(answer)


# 단축한 코드
def solution(s):
    return ' '.join([i.capitalize() for i in s.split(" ")])


q = solution("3people unFollowed me")
assert q == "3people Unfollowed Me"
print(q)

q = solution("for the last week")
assert q == "For The Last Week"
print(q)
