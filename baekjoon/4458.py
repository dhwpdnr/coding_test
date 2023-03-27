case = int(input())
answer = []
for _ in range(case):
    input_str = str(input())
    answer.append(input_str[0].upper() + input_str[1:])

for i in answer:
    print(i)
