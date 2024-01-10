p = input()

ppap = ["P", "P", "A", "P"]
stack = []
for i in p:
    stack.append(i)
    if stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append("P")

if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")
