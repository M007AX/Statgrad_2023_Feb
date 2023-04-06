Numbers = " 0123456789"
for x1 in range(10):
    for x2 in Numbers:
        for x3 in Numbers:
            for x4 in Numbers:
                word = "1" + str(x1) + "2655" + str(x2) + str(x3) + str(x4) + "8"
                word = word.replace(" ", "")
                if int(word) <= 10**10 and int(word) % 4173 == 0:
                    print(word)
