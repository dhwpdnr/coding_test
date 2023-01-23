def solution(cipher, code):
    answer = ''
    i = code - 1
    while i < len(cipher):
        answer += cipher[i]
        i += code
    return answer

    # 프로그래머스 연습문제 암호해독
