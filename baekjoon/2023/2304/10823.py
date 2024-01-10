nums = ""
while True:
    try:
        s = str(input())
        nums += s
    except:
        break

nums = list(map(int, nums.split(",")))

print(sum(nums))
