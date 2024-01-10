m = int(input())
n = int(input())
num = []
i = (m ** (1 / 2)) // 1
while i ** 2 <= n:
    if m <= i ** 2 <= n:
        num.append(int(i ** 2))
    i += 1
if num == []:
    print(-1)
else:
    print(sum(num))
    print(num[0])
