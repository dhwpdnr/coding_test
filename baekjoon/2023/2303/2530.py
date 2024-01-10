hour, minute, second = map(int, input().split())
add = int(input())
add_minute, add_second = divmod(add, 60)
add_hour, add_minute = divmod(add_minute, 60)
second += add_second
minute += add_minute
hour += add_hour
_minute, second = divmod(second, 60)
minute += _minute
_hour, minute = divmod(minute, 60)
hour += _hour
hour = hour % 24
print(hour, minute, second)