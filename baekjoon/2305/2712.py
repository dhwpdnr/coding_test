case = int(input())
arr = []

for _ in range(case):
    value, unit = map(str, input().split())
    if unit == "kg":
        arr.append(f"{float(value) * 2.2046:.4f} lb")
    elif unit == "lb":
        arr.append(f"{float(value) * 0.4536:.4f} kg")
    elif unit == "l":
        arr.append(f"{float(value) * 0.2642:.4f} g")
    elif unit == "g":
        arr.append(f"{float(value) * 3.7854:.4f} l")

for i in arr:
    print(i)
