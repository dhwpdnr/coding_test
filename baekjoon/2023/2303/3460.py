case = int(input())
for _ in range(case):
    n = int(input())
    binaryNum = format(n, 'b')
    for i in range(len(binaryNum)):
        if binaryNum[-i - 1] == "1":
            print(i, end=" ")
