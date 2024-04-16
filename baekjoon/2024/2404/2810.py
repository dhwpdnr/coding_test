n = int(input())

seat = input()

seat = seat.replace("LL", "S")

print(min(n, len(seat) + 1))
