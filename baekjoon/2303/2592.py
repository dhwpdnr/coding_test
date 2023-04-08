from collections import Counter

arr = [int(input()) for _ in range(10)]
counter_arr = Counter(arr)

print(sum(arr) // len(arr))
print(counter_arr.most_common(1)[0][0])
