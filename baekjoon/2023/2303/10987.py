n = str(input())

arr = ["a", "e", "i", "o", "u"]
count = 0
for i in arr:
    count += n.count(i)

print(count)
