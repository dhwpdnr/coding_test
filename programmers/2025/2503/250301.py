# 프로그래머스
# 코딩테스트 연습 > 2025 프로그래머스 코드챌린지 1차 예선 > 유연근무제
# https://school.programmers.co.kr/learn/courses/30/lessons/388351

def convertTime(n):
    h = n // 100
    m = n % 100
    return h * 60 + m


def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        s = startday
        schedule = convertTime(schedules[i])
        for time in timelogs[i]:
            if s in [6, 7]:
                s += 1
                if s == 8:
                    s = 1
                continue
            t = convertTime(time)
            if schedule + 10 < t:
                break
            else:
                s += 1
        else:
            answer += 1

    return answer


q = solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809],
                                [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5)
assert q == 3
print(q)

q = solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835],
                                    [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1)
assert q == 2
print(q)
