n = str(input())
res = ''
for i in n:
    if i == ' ' or ord(i) < ord('A'):
        res += i
    else:
        if ord(i) + 13 > 122:
            res += chr(96 + (ord(i) + 13) - 122)
        elif ord(i) + 13 > 90 and ord(i) < 91:
            res += chr(64 + (ord(i) + 13) - 90)
        else:
            res += chr(ord(i) + 13)
print(res)
