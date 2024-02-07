def get_reverse(s):
    if s == "1" or s == "8":
        return s
    elif s == "2":
        return "5"
    elif s == "5":
        return "2"
    else:
        return "?"


case, n = input().split()
n = int(n)
arr = []

for _ in range(n):
    arr.append(list(input().split()))

if case == "D" or case == "U":
    arr.reverse()
    for i in arr:
        print(" ".join([get_reverse(j) for j in i]))
else :
    for i in arr:
        i.reverse()
        print(" ".join([get_reverse(j) for j in i]))
