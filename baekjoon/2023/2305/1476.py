# 기존 코드

year = list(map(int, input().split()))

set_year = [1, 1, 1]
answer = 1
while True:
    if set_year == year:
        break

    answer += 1
    set_year[0] += 1
    set_year[1] += 1
    set_year[2] += 1
    if set_year[0] == 16:
        set_year[0] = 1
    if set_year[1] == 29:
        set_year[1] = 1
    if set_year[2] == 20:
        set_year[2] = 1

print(answer)

# while 조건 개선

year = list(map(int, input().split()))

set_year = [1, 1, 1]
answer = 1
while set_year != year:

    answer += 1
    set_year[0] += 1
    set_year[1] += 1
    set_year[2] += 1
    if set_year[0] == 16:
        set_year[0] = 1
    if set_year[1] == 29:
        set_year[1] = 1
    if set_year[2] == 20:
        set_year[2] = 1

print(answer)
