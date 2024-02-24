# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 코딩테스트 연습 > 해시 > 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True


q = solution(["119", "97674223", "1195524421"])
assert q == False
print(q)

q = solution(["123", "456", "789"])
assert q == True
print(q)

q = solution(["12", "123", "1235", "567", "88"])
assert q == False
print(q)
