arr = []
while True:
    s1 = str(input())
    s2 = str(input())
    if s1 == "END":
        break
    else:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        if s1 == s2:
            arr.append("same")
        else:
            arr.append("different")
for index, i in enumerate(arr):
    print(f"Case {index + 1}: {i}")
