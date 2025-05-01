import sys

K = int(sys.stdin.readline())

height = []
width = []
total = []

for i in range(6):
    dir, length = map(int, sys.stdin.readline().split())
    if dir == 1 or dir == 2:
        width.append(length)
        total.append(length)
    else:
        height.append(length)
        total.append(length)

bigbox = max(height) * max(width)

max_hidx = total.index(max(height))
max_widx = total.index(max(width))

small1 = abs(total[max_hidx - 1] - total[(max_hidx - 5 if max_hidx == 5 else max_hidx + 1)])

small2 = abs(total[max_widx - 1] - total[(max_widx - 5 if max_widx == 5 else max_widx + 1)])
area = bigbox - (small1 * small2)
print(area * K)
