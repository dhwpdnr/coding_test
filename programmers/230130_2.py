def solution(my_str, n):
    answer = []
    i = 0
    while i < len(my_str):
        if i + n > len(my_str):
            answer.append(my_str[i:])
        else:
            answer.append(my_str[i:i + n])
        i += n
    return answer

    # 프로그래머스 연습문제 잘라서 배열로 저장하기


def another(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

    # 리스트 컴프리헨션
