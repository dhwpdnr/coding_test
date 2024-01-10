def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 3131, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day[(sum(month[:a - 1]) + b) % 7]

    # 프로그래머스 연습문제 2016년
