import datetime

month, date = map(int, input().split())

date = datetime.datetime(2007, month, date)

print(date.strftime("%a").upper())
