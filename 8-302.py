from itertools import product

counter = 0
for i in product("EO", repeat = 12):
    s = "".join(i)
    if s.count("O") == 3 and not("OO" in s):
        if s[0] == "O":
            counter += 4**12
        else:
            counter += 3*4**11
print(counter)

"""
Result:
1660944384
"""