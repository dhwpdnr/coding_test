case = int(input())
member_lst = []

for _ in range(case):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key=lambda x: x[0])

for i in member_lst:
    print(i[0], i[1])
