arr = [350.34, 230.90, 190.55, 125.30, 180.90]

case = int(input())

answer = []

for _ in range(case):
    parts = list(map(float, input().split()))
    price = 0
    for i, k in zip(arr, parts):
        price += i * k

    answer.append(price)

for a in answer:
    print("${:.2f}".format(a))
