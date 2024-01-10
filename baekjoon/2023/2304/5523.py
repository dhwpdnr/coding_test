from sys import stdin

case = int(input())
a_win = 0
b_win = 0
for _ in range(case):
    a_score, b_score = map(int, stdin.readline().split())
    if a_score > b_score:
        a_win += 1
    elif a_score < b_score:
        b_win += 1

print(a_win, b_win)
