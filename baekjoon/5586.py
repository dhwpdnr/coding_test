input_str = str(input())

a = 0
b = 0

for index, i in enumerate(input_str):
    if i == "J":
        if input_str[index: index+3] == "JOI":
            a += 1
    if i == "I":
        if input_str[index: index+3] == "IOI":
            b += 1
print(a)
print(b)
