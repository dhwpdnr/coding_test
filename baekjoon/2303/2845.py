area, num = map(int, input().split())
people = area * num
news_people = list(map(int, input().split()))

for i in news_people:
    print(i - people, end=" ")
