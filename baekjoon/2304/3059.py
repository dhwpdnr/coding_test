case = int(input())

answer = []

for _ in range(case):
    str_input = str(input())
    n = 0
    for i in range(65, 91):
        if chr(i) not in str_input:
            n += i
    answer.append(n)

for k in answer:
    print(k)
