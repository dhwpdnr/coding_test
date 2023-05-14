answers = []

for i in range(3):
    fh, fm, fs, lh, lm, ls = map(int, input().split())
    first = (fh * 3600) + (fm * 60) + fs
    last = (lh * 3600) + (lm * 60) + ls
    time = last - first
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60
    answers.append(f"{h} {m} {s}")

for answer in answers:
    print(answer)
