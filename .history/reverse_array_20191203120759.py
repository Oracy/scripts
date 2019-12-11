def reverseArray(a):
    data = list(reversed(a))
    # print(*data, sep=' ')
    res = *data, sep=' '
    return res


a = [1, 4, 3, 2]

reverseArray(a)
