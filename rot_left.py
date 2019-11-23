def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return a


d = 4
a = [1, 2, 3, 4, 5]

print(rotLeft(a, d))