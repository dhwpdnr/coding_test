from collections import Counter

a = str(input())

a = a.upper()

count_a = Counter(a)
list_a = count_a.most_common()
if len(list_a) > 1:
    if list_a[0][1] == list_a[1][1]:
        print("?")
    else:
        print(list_a[0][0])
else:
    print(list_a[0][0])
