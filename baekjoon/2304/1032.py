case = int(input())

command = list(input())
command_len = len(command)

for _ in range(case - 1):
    a = str(input())
    for i in range(command_len):
        if a[i] != command[i]:
            command[i] = "?"

print("".join(command))
