count = 0

for _ in range(8):
    row = list(input())
    if _ % 2 == 0:
        count += row[::2].count("F")
    else:
        count += row[1::2].count("F")

print(count)
