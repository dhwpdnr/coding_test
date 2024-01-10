a, b = map(str, input().split())
len_a, len_b = len(a), len(b)

if len_a > len_b:
    b = '0' * (len_a - len_b) + b
else:
    a = '0' * (len_b - len_a) + a

answer = ""

for i in range(len(a)):
    answer += str(int(a[i]) + int(b[i]))

print(answer)
