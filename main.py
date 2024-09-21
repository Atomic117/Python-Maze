global u
u = []


def checkLRow(a, b, c, d):
    if c[a][b-1] == "p":
        return True
    else:
        return False


def checkRRow(a, b, c, d):
    if c[a][b+1] == "p":
        return True
    else:
        return False


def checkUCol(a, b, c, d):
    if c[a+1][b] == "p":
        return True
    else:
        return False


def checkDCol(a, b, c, d):
    if c[a-1][b] == "p":
        return True
    else:
        return False


def doublePos(a, b):
    print()


def convertPos(a, b):
    d = str(a) + "#" + str(b)
    return d


def lookPos(a, b, c, d, e, f):
    p = [False, False, False, False]
    if a + 1 < c:
        p[0] = checkDCol(a, b, e, f)
    if a - 1 >= 0:
        p[1] = checkUCol(a, b, e, f)
    if b + 1 < d:
        p[2] = checkRRow(a, b, e, f)
    if a - 1 >= 0:
        p[3] = checkLRow(a, b, e, f)

    if p.count(True) > 1:
        for i in range(len(p)):
            if p[i]:
                if i == 0:
                    return a-1, b
                elif i == 1:
                    return a+1, b
                elif i == 2:
                    return a, b+1
                else:
                    print()
    elif True in p:
        for i in range(len(p)):
            if p[i]:
                if i == 0:
                    f.append(convertPos(a - 1, b))
                    return a-1, b, f
                elif i == 1:
                    f.append(convertPos(a + 1, b))
                    return a+1, b, f
                elif i == 2:
                    f.append(convertPos(a, b + 1))
                    return a, b+1, f
                else:
                    f.append(convertPos(a, b - 1))
                    return a, b-1, f
    else:
        return -1, -1, f




x = []
g = int(input("Please enter a number: "))
for i in range(g):
    x.append([])
    h = input("Enter line " + str(i+1)+": ")
    for j in h:
        x[i].append(j)
h = len(x[0])

