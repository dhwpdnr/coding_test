case = int(input())

file_dic = {}

for _ in range(case):
    name, extension = map(str, input().split("."))
    if extension in file_dic:
        file_dic[extension] += 1
    else:
        file_dic[extension] = 1

sort_file = sorted(file_dic.items())

for key, value in sort_file:
    print(key, value)
