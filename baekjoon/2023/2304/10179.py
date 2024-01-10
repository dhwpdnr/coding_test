case = int(input())

arr = []

for _ in range(case):
    price = float(input())
    arr.append(price * 0.8)

for i in arr:
    print("${:.2f}".format(i))
