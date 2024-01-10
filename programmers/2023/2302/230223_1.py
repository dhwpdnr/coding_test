a, b = map(int, input().strip().split(' '))
answer = ""
for i in range(b):
    for k in range(a):
        answer += "*"
    answer += "\n"
print(answer)

# 프로그래머스 연습문제 직사각형 별찍기
