n = int(input())

for i in range(n):
    t = int(input())
    total_c = 0
    total_g = 0
    for k in range(t):
        c, g = map(float, input().split())
        total_c += c
        total_g += c * g
    print(f"{int(total_c)} {round(total_g / total_c, 1)}")
