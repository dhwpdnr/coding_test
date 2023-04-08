a = [int(input()) for _ in range(10)]
b = [int(input()) for _ in range(10)]

a.sort(reverse=True)
b.sort(reverse=True)

print(sum(a[0:3]), sum(b[0:3]))