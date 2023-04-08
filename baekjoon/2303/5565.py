total = int(input())
price = 0
for i in range(9):
    input_price = int(input())
    price += input_price

print(total - price)
