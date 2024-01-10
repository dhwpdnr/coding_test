N, M = map(int, input().split())

pw_dict = {}

for _ in range(N):
    site, pw = map(str, input().split())
    pw_dict[site] = pw

for _ in range(M):
    print(pw_dict[str(input())])
