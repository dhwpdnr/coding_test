case = int(input())
answer = []
for _ in range(case):
    a, b = map(int, input().split())
    s = str(input())
    res = ''.join([chr(ord('A') + ((ord(c) - ord('A')) * a + b) % 26) for c in s])
    answer.append(res)

for i in answer:
    print(i)
