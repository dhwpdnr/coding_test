case = int(input())

for _ in range(case):
    Y = 0
    K = 0
    for _2 in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")
