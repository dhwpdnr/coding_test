str_input = str(input())

str_output = ""

for i in str_input:
    n = ord(i) - 3
    if n < 65:
        n = 91 - (65 - n)
    str_output += chr(n)

print(str_output)
