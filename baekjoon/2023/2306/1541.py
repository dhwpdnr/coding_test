exp = list(map(str, input().split('-')))

num = []

for i in exp:
    sum = 0
    tmp = list(map(str, i.split("+")))
    for j in tmp:
        sum += int(j)
    num.append(sum)

n = num[0]

for i in range(1, len(num)):  # 1번째 값부터 n에서 빼준다
    n -= num[i]
print(n)
