time = int(input())

minute_5, rest = divmod(time, 300)
minute_1, rest = divmod(rest, 60)
second_10, rest = divmod(rest, 10)
if rest != 0:
    print(-1)
else:
    print(minute_5, minute_1, second_10)
