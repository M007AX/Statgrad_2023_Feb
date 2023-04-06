f = open('17.txt')
a = [int(x) for x in f.readlines()]
mx = -10**20
for i in range(len(a)):
    if (abs(a[i]) % 7 == 0) and(a[i] > mx):
        mx = a[i]
print(mx)
k = 0
m= -10**40
for i in range(len(a) - 1):
    if ((abs(a[i]) % 7 == 0 and abs(a[i + 1]) % 7 != 0) or (abs(a[i]) % 7 != 0 and abs(a[i + 1]) % 7 == 0)) and abs(a[i]) % 10 == abs(a[i + 1]) % 10:
        if a[i]**2 + a[i + 1]**2 <= mx**2:
            k += 1
            m = max(a[i]**2 + a[i + 1]**2, m)
print(k, m)