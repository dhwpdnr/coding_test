L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C == 0:
    a = A // C
else:
    a = A // C + 1
if B % D == 0:
    b = B // D
else:
    b = B // D + 1

print(L - max(a, b))
