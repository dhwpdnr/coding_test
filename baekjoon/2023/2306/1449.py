n, l = map(int, input().split())

cracks = list(map(int, input().split()))

cracks.sort()

start = cracks[0]

count = 1

for location in cracks[1:]:
    if location in range(start, start + l):
        continue
    else:
        start = location
        count += 1
print(count)
