text = list(str(input()))

state = False
result = ""
stack = ""

for i in text:
    if state:
        stack += i
        if i == '>':
            state = False
            result += stack
            stack = ''
    else:
        if i == '<':
            state = True
            stack += i
        elif i == ' ':
            stack += i
            result += stack
            stack = ''
        else:
            stack = i + stack

print(result + stack)
