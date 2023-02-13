def solution(s):
    low_s = s.lower()
    p_count = low_s.count('p')
    y_count = low_s.count('y')

    if p_count == y_count:
        return True
    else:
        return False


    # 프로그래머스 연습문제 문자열 내 p와 y의 개수