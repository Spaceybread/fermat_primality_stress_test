p = 10000001
a = 2

potentials = []
rejects = []

while True:
    t1 = (a**(p - 1))%p
    t2 = 1%p

    if t1 == t2:
        potentials.append(p)
        print(p)
    else:
        rejects.append(p)

    i = p + 2
    t3 = (a**(i - 1))%i
    t4 = 1%i

    if t3 == t4:
        potentials.append(i)
        print(i)
    else:
        rejects.append(i)

    j = i + 2
    t5 = (a**(j - 1))%j
    t6 = 1%j

    if t5 == t6:
        potentials.append(j)
        print(j)
    else:
        rejects.append(j)


    p = p + 6
