case = int(input())

answer = 0

car = {}
out = []

for i in range(case):
    car[input()] = i

for _ in range(case):
    out.append(input())

for j in range(case - 1):
    for k in range(j + 1, case):
        if car[out[j]] > car[out[k]]:
            answer += 1
            break
print(answer)
