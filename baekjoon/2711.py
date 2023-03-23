case = int(input())
answer = []
for _ in range(case):
    index, word = map(str, input().split())
    index = int(index)
    answer.append(word[0:index - 1] + word[index:])
for i in answer:
    print(i)
