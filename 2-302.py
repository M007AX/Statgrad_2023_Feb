print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((w <= x) or (y <= z)) and ((x == y) <= (w == z))):
                    print(x, y, z, w)
"""                    
Result:
x y z w
0 0 0 1
0 0 1 0
0 1 0 1
1 1 0 1
1 1 1 0

Ans: xzwy
"""
