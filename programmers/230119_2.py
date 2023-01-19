def solution(my_string):
    answer = ''.join(dict.fromkeys(my_string))
    return answer

    # 프로그래머스 연습문제 중복된 문자 제거
