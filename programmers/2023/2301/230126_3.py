def solution(my_string):
    my_arr = my_string.split(" ")
    mode = True
    i = 0
    answer = 0
    while i < len(my_arr):
        if i == 0:
            answer += int(my_arr[i])
        else:
            if my_arr[i] == "+":
                mode = True
            elif my_arr[i] == "-":
                mode = False
            else:
                if mode:
                    answer += int(my_arr[i])
                else:
                    answer -= int(my_arr[i])
        i += 1
    return answer

    # 프로그래머스 연습문제 문자열 계산하기
