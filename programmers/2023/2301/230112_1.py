def solution(box, n):
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    answer = a * b *c
    return answer

    # 프로그래머스 주사위의 개수