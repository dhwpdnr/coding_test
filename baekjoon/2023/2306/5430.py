# 시간 초과
#
# from collections import deque
#
# case = int(input())
#
# answers = []
#
# for _ in range(case):
#     commands = input()
#     len_arr = int(input())
#     arr = deque(list(input()[1:-1].split(",")))
#
#     if len_arr == 0:
#         arr = deque()
#
#     status = True
#     for command in commands:
#         if command == "R":
#             arr.reverse()
#         elif command == "D":
#             if arr:
#                 arr.popleft()
#             else:
#                 status = False
#                 answers.append("error")
#                 break
#
#     if status:
#         answers.append("[" + ",".join(arr) + "]")
#
# for answer in answers:
#     print(answer)


# 개선

from collections import deque

case = int(input())

for i in range(case):
    commands = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    queue = deque(arr)

    flag = 0

    if n == 0:
        queue = []

    for command in commands:
        if command == 'R':
            flag += 1
        elif command == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")


