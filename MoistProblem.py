testCase = int(input())
ar = []
b = []
c = []
d = 0
k = []
for a in range(testCase):
    k.append(a + 1)
    cards = int(input())
    for i in range(cards):
        i = str(input())
        ar.append(i)
        b = ar
        ar = sorted(ar)
        if b != ar:
            d += 1
    c.append(d)
    b = []
    ar = []
    d = 0
for x in range(testCase):
    print("Case #" + str(k[x]) + ": " + str(c[x]))
