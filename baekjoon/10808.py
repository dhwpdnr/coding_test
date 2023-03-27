n = str(input())

arr = []
for i in range(97, 123):
    arr.append(str(n.count(chr(i))))

print(" ".join(arr))
