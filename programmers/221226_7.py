def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    if denum >= num:
        less = num
    else:
        less = denum

    for i in range(less, 0, -1):
        if num % i == 0 and denum % i == 0:
            gcd = i
            break

    answer = [denum / gcd, num / gcd]
    return answer

# 프로그래머스 코딩테스트 입문