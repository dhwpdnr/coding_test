player_1 = list(map(int, input().split()))
player_2 = list(map(int, input().split()))

win_1 = 0
win_2 = 0

for a, b in zip(player_1, player_2):
    if a > b:
        win_1 += 1
    elif a < b:
        win_2 += 1

if win_1 > win_2:
    print("A")
elif win_1 < win_2:
    print("B")
else:
    print("D")
