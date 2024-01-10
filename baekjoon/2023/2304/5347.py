import math

case = int(input())

answer = []
for _ in range(case):
    a, b = map(int, input().split())
    answer.append(math.lcm(a, b))

for i in answer:
    print(i)
