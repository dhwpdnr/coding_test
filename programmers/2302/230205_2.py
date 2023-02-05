def solution(chicken):
    answer = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div + mod
    return answer

    # 프로그래머스 연습문제 치킨 쿠폰
