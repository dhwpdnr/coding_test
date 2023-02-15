def solution(s):
    if s[0] == "-":
        i = -1
        ls = list(str(s[1:]))
    elif s[0] == "+":
        i = 1
        ls = list(str(s[1:]))
    else:
        i = 1
        ls = list(str(s))
    num = int("".join(ls))
    return num * i

    # 프로그래머스 연습문제 문자열을 정수로 바꾸기

def solution(s):
    return int(s)

    # 쉬운 풀이 int로 바꿔줄때 부호도 자연적으로 인식하는 듯 함