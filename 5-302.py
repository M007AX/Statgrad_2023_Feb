"""def chet(n):
    amount = 0
    n = str(int(n, 2))
    for x in range(len(n)):
        amount += int(n[x])
    if amount % 2 == 0:
        return True
    else:
        return False

counter = 0
for i in range(123456789, 265432098):
    n = bin(i)[2::]
    for j in range(3):
        if chet(n):
            n += "0"
        else:
            n += "1"
    R = int(n, 2)
    if R >= 987654321 and R <= 2123456790:
        print(R, i)
print(counter)"""
a = 123456789
b = 265432097
print(b - a)