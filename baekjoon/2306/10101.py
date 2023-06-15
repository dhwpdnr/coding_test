arr = [int(input()) for _ in range(3)]

if sum(arr) != 180:
    print("Error")
else:
    l = len(set(arr))
    if l == 1:
        print("Equilateral")
    elif l == 2:
        print("Isosceles")
    else:
        print("Scalene")
