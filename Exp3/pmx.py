import random

def order1(chromosome1, chromosome2) :
    N = len(chromosome1)
    child = list()
    idx0 = random.randrange(0, N)
    idx1 = random.randrange(0, N)
    
    lo, hi = 0, 0
    if idx0 < idx1 :
        lo = idx0
        hi = idx1
    else :
        lo = idx1
        hi = idx0

    fragment = chromosome1[lo : hi + 1]

    for i in range(N) :
        if chromosome2[i] not in fragment :
            child.append(chromosome2[i])

    insertion = random.randint(0, len(child))
    print(fragment)
    child = child[:insertion] + fragment + child[insertion:]
    return child


def PMX(chromosome1, chromosome2) :
    N = len(chromosome1)
    child = chromosome2.copy()
    idx0 = random.randrange(0, N)
    idx1 = random.randrange(0, N)
    
    lo, hi = 0, 0
    if idx0 < idx1 :
        lo = idx0
        hi = idx1
    else :
        lo = idx1
        hi = idx0
    
    child[lo : hi + 1] = chromosome1[lo : hi + 1]
    print(child[lo : hi + 1])
    for i in range(hi - lo + 1) :
        if chromosome2[lo + i] not in child[lo : hi + 1] :
            value = chromosome1[lo + i]
            position = chromosome2.index(value)
            while(position >= lo and position <= hi) :
                value = chromosome1[position]
                position = chromosome2.index(value)
            child[position] = chromosome2[lo + i]
    return child

N = 10
a = [i for i in range(N)]
b = [i for i in range(N)]
random.shuffle(a)
random.shuffle(b)
c= order1(a, b)
print(a)
print(b)
print(c)