def solution(num, total):
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 2)//2)]

    # 프로그래머스 연습문제 연속된 수의 합