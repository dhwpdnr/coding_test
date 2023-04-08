answer = []
for _ in range(3):
    arr = list(map(int, input().split()))
    answer.append(arr)
for i in answer:
    count_0 = i.count(0)
    count_1 = i.count(1)
    if count_0 == 1 and count_1 == 3:
        print("A")
    elif count_0 == 2 and count_1 == 2:
        print("B")
    elif count_0 == 3 and count_1 == 1:
        print("C")
    elif count_0 == 4 and count_1 == 0:
        print("D")
    elif count_0 == 0 and count_1 == 4:
        print("E")
