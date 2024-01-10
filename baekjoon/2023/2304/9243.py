case = int(input())

a = list(map(int, input()))
b = list(map(int, input()))

if case % 2 == 0:
    if a == b:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    check = False
    for i, j in zip(a, b):
        if i == j:
            check = True
            break
    if check:
        print("Deletion failed")
    else:
        print("Deletion succeeded")
