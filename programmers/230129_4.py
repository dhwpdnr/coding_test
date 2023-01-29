def solution(my_string):
    lower_str = my_string.lower()
    str_list = list(lower_str)
    str_list.sort()
    answer = ''.join(str_list)
    return answer

    # 프로그래머스 연습문제 문자열 정렬하기(2)