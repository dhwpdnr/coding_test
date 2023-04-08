arr = []

while True:
    try:
        a = str(input())
        arr.append(a)
    except:
        break

for i in arr:
    print(i)
