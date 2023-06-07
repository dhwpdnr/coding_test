from collections import Counter

n = int(input())
cards = Counter(list(map(int, input().split())))
m = int(input())
check_arr = list(map(int, input().split()))

for i in check_arr:
    print(cards[i], end=" ")
