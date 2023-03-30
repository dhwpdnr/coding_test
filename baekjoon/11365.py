arr = []
while True:
    a = str(input())
    if a == "END":
        break
    else:
        arr.append(a)

for i in arr:
    print(i[::-1])
