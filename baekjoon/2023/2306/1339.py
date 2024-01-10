case = int(input())
words = []
for _ in range(case):
    words.append(input())

word_dict = {}

for word in words:
    square_root = len(word) - 1
    for c in word:
        if c in word_dict:
            word_dict[c] += pow(10, square_root)
        else:
            word_dict[c] = pow(10, square_root)
        square_root -= 1

word_dict = sorted(word_dict.values(), reverse=True)

result, m = 0, 9

for value in word_dict:
    result += value * m
    m -= 1

print(result)
