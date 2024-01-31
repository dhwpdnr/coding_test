import sys

input = sys.stdin.readline

n, m = map(int, input().split())

group_dict = {}

for _ in range(n):
    team = input().rstrip()
    member_count = int(input())
    member = [input().rstrip() for i in range(member_count)]
    # print(member)
    group_dict[team] = sorted(member)
for _ in range(m):
    quiz = input().rstrip()
    type = int(input())
    if type == 1:
        print(''.join([k for k, v in group_dict.items() if quiz in v]))
    else:
        print('\n'.join(*[v for k, v in group_dict.items() if quiz in k]))
