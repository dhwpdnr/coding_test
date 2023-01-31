def solution(my_string, num1, num2):
    list_string = list(my_string)
    n1 = list_string[num1]
    n2 = list_string[num2]
    list_string[num1] = n2
    list_string[num2] = n1
    answer = ""
    for i in list_string:
        answer += i
    return answer

    # 프로그래머스 연습문제 인덱스 바꾸기
