import random
import matplotlib.pyplot as plt
import time

def generatemymap(N) :
    mymap = list()
    for i in range(N) :
        mymap.append([0] * N)
    for i in range(N) :
        for j in range(i, N) :
            if i == j :
                continue
            w = random.randrange(1, 1000)
            mymap[i][j] = w
            mymap[j][i] = w
    return mymap

LENGTH = 100
MAP = generatemymap(LENGTH)

def overhead(sequence, mymap) :
    N = len(sequence)
    distance = 0
    for i in range(N - 2) :
        distance += mymap[i][i+1]
    distance += mymap[sequence[0]][sequence[N-1]]
    return distance


def footrule(a, b) :
    distance = 0
    for i in range(len(a)) :
        if a[i] != b[i] :
            distance += 1
    return distance

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
    for i in range(hi - lo + 1) :
        if chromosome2[lo + i] not in child[lo : hi + 1] :
            value = chromosome1[lo + i]
            position = chromosome2.index(value)
            while(position >= lo and position <= hi) :
                value = chromosome1[position]
                position = chromosome2.index(value)
            child[position] = chromosome2[lo + i]
    return child

class individual :
    def __init__(self) :
        self.dim = LENGTH
        self.chromosome = [i for i in range(self.dim)]
        random.shuffle(self.chromosome)
        self.fit = self.fitness()

    def fitness(self) :
        return overhead(self.chromosome, MAP)

    def setchromosome(self, chromosome) :
        self.chromosome = chromosome
        self.fit = self.fitness()

class ga :
    def __init__(self, population, max_iter) :
        self.individuals = list()
        self.dim = LENGTH
        self.max_iter = max_iter
        self.currentbest = list()
        self.population = population
        self.bestvalues = list()
        self.besttrace = list()

        for i in range(population) :
            self.individuals.append(individual())
    
    def optimize(self) :
        self.currentbest.clear()
        self.bestvalues.clear()
        self.besttrace.clear()

        for iter in range(self.max_iter) :
            print('iter=' + str(iter), end=' ')
            nextgen = list()
            # Roulette Wheel selection, retain 10% best individuals
            self.individuals = sorted(self.individuals, key = lambda item : item.fit)
            self.currentbest.append(self.individuals[0].fit)

            if self.bestvalues != [] :
                if self.individuals[0].fit < self.bestvalues[-1] :
                    self.bestvalues.append(self.individuals[0].fit)
                    self.besttrace.append(self.individuals[0].chromosome)
                else :
                    self.bestvalues.append(self.bestvalues[-1])
                    self.besttrace.append(self.besttrace[-1])
            else :
                self.bestvalues.append(self.individuals[0].fit)
                self.besttrace.append(self.individuals[0].chromosome)

            for i in range(int(self.population * 0.1)) :
                nextgen.append(self.individuals[i])
            print(self.bestvalues[-1], end='\n')

            # sum_fit = 0
            # for i in range(self.population) :
            #     sum_fit += self.individuals[i].fit
            
            # wheel = list()
            # for i in range(self.population) :
            #     wheel.append(self.individuals[i].fit / sum_fit)
            
            while(len(nextgen) < self.population) :
                # p = random.uniform(0, 1) 
                # parent1 = 0
                # for i in range(self.population) :
                #     if p > wheel[i] :
                #         parent1 = i
                # parent2 = parent1
          
                # while(parent2 == parent1) :
                #     p = random.uniform(0, 1) 
                #     for i in range(self.population) :
                #         if p > wheel[i] :
                #             parent2 = i
                parent1 = random.randrange(0, self.population)
                parent2 = parent1
                while(parent2 == parent1) :
                    parent2 = random.randrange(0, self.population)
                
                childchromosome = order1(self.individuals[parent1].chromosome, 
                                    self.individuals[parent2].chromosome)

                child = individual()
                child.setchromosome(childchromosome)
                nextgen.append(child)
                # !!
            self.individuals = nextgen


iterations = 100
population = 30

optimizer = ga(population, iterations)
time_start = time.time() 
optimizer.optimize()
time_end = time.time()
time_c1= time_end - time_start
x1 = range(iterations)
y1 = optimizer.bestvalues

fig = plt.figure()
ax1 = plt.subplot(2, 1, 1)
ax1.plot(x1, y1, label = 'best_value')
ax1.set_xlabel('iterations')
plt.setp(ax1.get_xticklabels(), fontsize=6)

ax1.legend()

ax1.set_title('GA: Time Consumed: ' + str(time_c1) + 
's\n best value: ' + str(optimizer.bestvalues[-1]))

ax2 = plt.subplot(2, 1, 2)
x2 = range(iterations)
y2 = list()
for i in x2 :
    y2.append(footrule(optimizer.besttrace[-1], optimizer.besttrace[i]))
ax2.plot(x2, y2, label = 'distance')
ax2.set_xlabel('iterations')
ax2.legend()
print(optimizer.bestvalues[0])

plt.show()
