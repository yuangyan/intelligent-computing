import random

def generatemap(N) :
    map = list()
    for i in range(N) :
        map.append([0] * N)
    for i in range(N) :
        for j in range(i, N) :
            if i == j :
                continue
            w = random.randrange(1, 10000)
            map[i][j] = w
            map[j][i] = w
    return map

map = generatemap(5)
print(map[1][1])

