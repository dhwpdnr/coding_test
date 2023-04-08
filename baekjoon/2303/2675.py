n = int(input())
result = []
for i in range(n):
    num, input_string = map(str, input().split())
    num = int(num)
    result_string = ""
    for s in input_string:
        result_string += s * num
    result.append(result_string)
for i in result:
    print(i)
