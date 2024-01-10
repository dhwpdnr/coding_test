def solution(polynomial):
    x, num = 0, 0
    polynomial = polynomial.replace(" ", "").split("+")
    for i in polynomial:
        if i.isnumeric():
            num += int(i)
        else:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
    result = []
    if x:
        if x == 1:
            result.append('x')
        else:
            result.append(f'{x}x')
    if num:
        result.append(f'{num}')
    return ' + '.join(result)

    # 프로그래머스 연습문제 다항식 더하기
