def solution(bin1, bin2):
    sum = int(bin1, 2) + int(bin2, 2)
    return str(bin(sum))[2:]

    # 프로그래머스 연습문제 이진수 더하기