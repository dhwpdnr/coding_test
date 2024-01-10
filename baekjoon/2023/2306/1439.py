str_in = input()
count = 0
prev = '?'
for i in str_in:
    if i != prev:
        prev = i
        count += 1

print(count // 2)
