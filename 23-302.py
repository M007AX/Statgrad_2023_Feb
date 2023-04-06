def f(x, y, n):
    if x > y or x == 15:
        return 0
    if x == y and n > 0:
        return 1
    else:
        return f(x + 1, y, n) + f(x + 2, y, n) + f(x*2, y, n + 1)+ f(x*3, y, n + 1)
print(f(1, 10, 0))