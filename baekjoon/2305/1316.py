case = int(input())

answer = case

for _ in range(case):
    word = str(input())
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 1:]:
            case -= 1
            break

print(case)
