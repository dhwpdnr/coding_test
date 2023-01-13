def solution(my_string):
    answer = []
    for i in my_string :
        if i == "0" :
            answer.append(int(i))
        elif i == "1":
            answer.append(int(i))
        elif i == "2":
            answer.append(int(i))
        elif i == "3":
            answer.append(int(i))
        elif i == "4":
            answer.append(int(i))
        elif i == "5":
            answer.append(int(i))
        elif i == "6":
            answer.append(int(i))
        elif i == "7":
            answer.append(int(i))
        elif i == "8":
            answer.append(int(i))
        elif i == "9":
            answer.append(int(i))
    sums = 0
    for k in answer:
        sums += k
    return sums

    # 프로그래머스 연습문제 숨어있는 숫자의 덧샘