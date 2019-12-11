def reverseArray(a):
    data = list(reversed(a))
    res = *data, sep = ' '
    print(res)
    return res


a = [1, 4, 3, 2]
reverseArray(a)
print()
