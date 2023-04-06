"""def F(a, b):
    if a == 0 and b == 0:
        return 0
    if a > b:
        return F(a - 1, b) + b
    if a <= b and b > 0:
        return F(a, b - 1) + a

заметим, что значения - перемноженные a и b

for a in range(100):
    for b in range(100):
        print(F(a, b))
        print(a, b)"""
"""counter = 0
c = 2097152
A = []
for i in range(1, 1449):
    if c % i == 0:
        counter += 1
print(counter)
всего 11 делителей до квадрата, а к ним есть пары после квадрата, значит ответ 11 для a и для b получается 22"""
