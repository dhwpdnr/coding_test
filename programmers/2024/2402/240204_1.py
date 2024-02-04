# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 코딩테스트 연습 > 스택/큐 > 기능개발

def solution(progresses, speeds):
    answer = []
    days = []
    stack = []
    for p, s in zip(progresses, speeds):
        left_per = 100 - p
        a, b = divmod(left_per, s)
        days.append(a) if b == 0 else days.append(a + 1)
    for i in days:
        if stack == []:
            stack.append(i)
        elif stack[0] >= i:
            stack.append(i)
        else:
            answer.append(len(stack))
            stack = [i]
    answer.append(len(stack))
    return answer


# 실제 일자를 증가시켜 앞에서 부터 처리하는 방법
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


q = solution([93, 30, 55], [1, 30, 5])
assert q == [2, 1]
print(q)

q = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
assert q == [1, 3, 2]
print(q)
