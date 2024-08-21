n = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())
t_bundle = 0

for i in lst:
    if i == 0:
        continue
    elif i <= T:
        t_bundle += 1
    elif i % T == 0:
        t_bundle += i // T
    else:
        t_bundle += i // T + 1

p_bundle = n // P
pen = n % P

print(t_bundle)
print(f'{p_bundle} {pen}')
