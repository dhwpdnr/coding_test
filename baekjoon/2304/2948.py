import datetime

date, month = map(int, input().split())

date = datetime.datetime(2009, month, date)

print(str(date.strftime("%A")))
