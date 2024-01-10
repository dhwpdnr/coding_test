resist = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

arr = [input() for _ in range(3)]

print((resist.index(arr[0]) * 10 + resist.index(arr[1])) * (10 ** resist.index(arr[2])))
