def reverseArray(a):
    data = list(reversed(a))
    res = *data, sep = ' '
    print(*data, sep=' ')
    return res


a = [1, 4, 3, 2]

reverseArray(a)
