while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    else:
        arr.sort()
        l = len(set(arr))
        if arr[-1] >= arr[0] + arr[1]:
            print("Invalid")
        else:
            if l == 1:
                print("Equilateral")
            elif l == 2:
                print("Isosceles")
            else:
                print("Scalene")
