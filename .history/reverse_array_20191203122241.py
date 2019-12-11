def reverseArray(a):
    data = list(reversed(a))
    res = ''.join(str(x) for x in data)
    return res


a = [1, 4, 3, 2]

print(reverseArray(a))