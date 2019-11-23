def minimumBribes(q):
    bribe = 0
    for position in range(len(q)):
        print('index: {}'.format(q.index(q[position])+1))
        print('q: {}'.format(q[position]))
        if q[position] <= q.index(q[position])+2:
            bribe += q.index(q[position])+1 - q[position]
            print('Posicao Correta')
        # else:
            # return print('Too chaotic')
        # print(q.index(q[position])+1)
    return bribe, q





n = 5
q = [2, 1, 5, 3, 4]
# n = 5
# q = [2, 5, 1, 3, 4]

print(minimumBribes(q))