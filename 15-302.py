def f(x, a):
    return ((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & a != 0))


for a in range(1, 300):
    p = True
    for x in range(0, 300):
        if f(x, a) == False:
            p = False
            break
    if p == True:
        print(a)
        break