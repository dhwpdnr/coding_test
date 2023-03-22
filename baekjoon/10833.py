case = int(input())
student = []
apple = []
for _ in range(case):
    a, b = map(int, input().split())
    student.append(a)
    apple.append(b)
answer = 0
for i, k in zip(apple, student):
    answer += i % k
print(answer)
