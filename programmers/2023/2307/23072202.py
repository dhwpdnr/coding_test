def solution(a, b):
    a1 = int(str(a) + str(b))
    a2 = 2 * a * b
    if a1 < a2:
        return a2
    return a1