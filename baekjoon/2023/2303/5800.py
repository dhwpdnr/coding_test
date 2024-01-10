case = int(input())
max_scores = []
min_scores = []
gaps = []

for _ in range(case):
    scores = list(map(int, input().split()))
    scores.pop(0)
    scores.sort()
    min_scores.append(scores[0])
    max_scores.append(scores[-1])
    gap = 0
    for i in range(1, len(scores)):
        if scores[i] - scores[i - 1] > gap:
            gap = scores[i] - scores[i - 1]
    gaps.append(gap)

for k in range(case):
    print(f"Class {k + 1}")
    print(f"Max {max_scores[k]}, Min {min_scores[k]}, Largest gap {gaps[k]}")
