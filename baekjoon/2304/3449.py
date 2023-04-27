case = int(input())

answer = []

for _ in range(case):
    a = input()
    b = input()
    count = 0
    for i, k in zip(a, b):
        if i != k:
            count += 1
    answer.append(count)

for i in answer:
    print(f"Hamming distance is {i}.")
