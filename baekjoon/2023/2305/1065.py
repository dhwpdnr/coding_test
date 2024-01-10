n = int(input())

answer = 0

for i in range(1, n + 1):
    if i < 100:
        answer += 1
    else:
        number_list = list(map(int, str(i)))
        if number_list[1] - number_list[0] == number_list[2] - number_list[1]:
            answer += 1

print(answer)
