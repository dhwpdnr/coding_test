range_num = set(x for x in range(1, 10001))
check_num = set()

for i in range(1, 10001):
    for k in str(i):
        i += int(k)
    check_num.add(i)

self_num = sorted(range_num - check_num)

for t in self_num:
    print(t)
