def solution(price, money, count):
    pay = 0
    for i in range(1, count + 1):
        pay += i * price
    if pay <= money:
        return 0
    return pay - money

    # 프로그래머스 연습문제 부족한 금액 계산하기


def solution(price, money, count):
    pay = 0
    for i in range(1, count + 1):
        pay += i * price
    return max(0, pay - money)

    # 마지막 if 문 max 로 처리
