case = int(input())
for _ in range(case):
    n = int(input())
    max = 0
    mName = ""
    for _ in range(n):
        name, num = input().split()
        num = int(num)
        if(num > max):
            max = num
            mName = name
    print(mName)