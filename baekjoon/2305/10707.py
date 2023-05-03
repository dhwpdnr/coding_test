x_liter = int(input())
y_normal = int(input())
y_limit = int(input())
y_liter = int(input())
use = int(input())

if use <= y_limit:
    print(min(x_liter * use, y_normal))
else:
    print(min(x_liter * use, y_normal + y_liter * (use - y_limit)))
