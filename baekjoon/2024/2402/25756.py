n = int(input())

arr = list(map(int, input().split()))

v = 0

for i in arr:
    v_now = (1 - (1 - v / 100) * (1 - i / 100)) * 100
    print(v_now)
    v = v_now
