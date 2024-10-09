import sys

hurt_finger = int(sys.stdin.readline())
max_repeat = int(sys.stdin.readline())
answer = 0

if hurt_finger == 1:
    if max_repeat == 0:
        answer += hurt_finger - 1
    else:
        answer += 8 * max_repeat
elif hurt_finger == 5:
    if max_repeat == 0:
        answer += hurt_finger - 1
    else:
        answer += 4 + 8 * (max_repeat)


else:
    if max_repeat == 0:
        answer += hurt_finger - 1
    else:
        answer += 4 * (max_repeat) + 1
        if max_repeat % 2 == 0:
            answer += hurt_finger - 2
        else:
            answer += 4 - hurt_finger

print(answer)
