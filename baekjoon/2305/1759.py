from itertools import combinations

L, C = map(int, input().split())

arr = sorted(list(map(str, input().split())))

vowels = ["a", "e", "i", "o", "u"]

combi = combinations(arr, L)
answers = []

for case in combi:
    vowel_cnt = 0
    const_cnt = 0
    for i in case:
        if i in vowels:
            vowel_cnt += 1
        else:
            const_cnt += 1
    if vowel_cnt > 0 and const_cnt > 1:
        answers.append("".join(case))

answers.sort()

for answer in answers:
    print(answer)
