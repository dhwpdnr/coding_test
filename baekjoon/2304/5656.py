answer = []
while True:
    arr = list(map(str, input().split()))
    if arr[1] == ">":
        answer.append(int(arr[0]) > int(arr[2]))
    elif arr[1] == ">=":
        answer.append(int(arr[0]) >= int(arr[2]))
    elif arr[1] == "<":
        answer.append(int(arr[0]) < int(arr[2]))
    elif arr[1] == "<=":
        answer.append(int(arr[0]) <= int(arr[2]))
    elif arr[1] == "==":
        answer.append(int(arr[0]) == int(arr[2]))
    elif arr[1] == "!=":
        answer.append(int(arr[0]) != int(arr[2]))
    elif arr[1] == "E":
        break

for index, i in enumerate(answer):
    if i:
        print(f"Case {index+1}: true")
    else:
        print(f"Case {index+1}: false")
