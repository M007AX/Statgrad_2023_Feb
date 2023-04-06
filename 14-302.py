alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for p in range(2, 37):
    for x in alphabet:
        for y in alphabet:
            first = x + x + x + "8"
            second = "43" + x + "9"
            ans = y + y + "04"
            try:
                if int(first, p) + int(second, p) == int(ans, p):
                    print(int(y + y + x, p))
            except:
                continue