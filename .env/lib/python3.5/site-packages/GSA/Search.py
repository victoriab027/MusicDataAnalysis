import numpy as np

def distance(xi, xj):
    # returns Euclidean distance between two point i and j
    return np.linalg.norm(xi-xj)

def fitness(Points, label, particle):

    #Points : All Point Coordinates
    #Label : All Point Labels
    #Particle : The Solution Particle
    fitness = 0

    for i in range(len(Points)):
        cluster_no = label[i]
        centroid = particle[int(cluster_no) * len(Points[i]):(int(cluster_no) + 1) * len(Points[i])]
        fitness += distance(Points[i], centroid) ** 2

    return fitness

def Fitness_for_All(Particles, Labels, Points):
    # Candidate Solution =n*s
    Total_fitness = []

    for i in range(len(Particles)):
        Total_fitness.append(fitness(Points, Labels, Particles[i]))

    return Total_fitness

#Custom
def FitnessAll(Particles,Data,custom,d,k):
    # Candidate Solution =n*s
    Total_fitness = []

    for i in range(len(Particles)):
        Total_fitness.append(custom(Data, Particles[i].reshape(d,k)))

    return Total_fitness


def Mass(Particles,Total_fitness,problem_type,epsilon):

    Masses = []
    #For Minimisation Problem
    if(problem_type=='min'):
        worst = max(Total_fitness)

        den = 0
        for i in range(len(Total_fitness)):
            den += Total_fitness[i] - worst
    else:
        #For Maximisation Problem
        worst=min(Total_fitness)

        den=0
        for i in range(len(Total_fitness)):
            den+=Total_fitness-worst

    for i in range(len(Particles)):
        Masses.append((Total_fitness[i] - worst) / (den + epsilon))

    return Masses

def acc(Particles, Masses, rj, G, iters,epsilon):
    #Calculation of  Acceleration
    kbest = len(Particles) - iters
    # For every D dimension

    ds = sorted(Masses, reverse=True)
    # ds=sorted(range(len(M),key= lambda k:M[k],reverse=True)
    force = np.ndarray(Particles.shape, dtype=np.float64)

    for i in range(len(Particles)):
        Fi = np.ndarray((1, Particles.shape[1]), dtype=np.float64)
        # print(Fi.shape,(1,Particles.shape[1]))
        for j in range(kbest):
            if (j != i):
                # print(Fi.shape,Particles.shape)
                Fi += rj * G * Masses[j] * (Particles[i] - Particles[j]) / (
                            distance(Particles[i], Particles[j]) + epsilon)
        # print(force.shape)
        force[i, :] = Fi
    return force

def velocity(vel, acc, ri):

    # Calculating velocity

    vel = vel * ri + acc

    return vel


def Update(Particles, vel):

    #Updating Particle Position

    Particles = Particles + vel

    return Particles

def Generate_Solutions(Range, init_population,solution_dimension, seed_particle):
    #Generating Random Solution
    l = Range[0]
    r = Range[1]
    #print('L ',l)
    #print('R ',r)
    np.random.seed(seed_particle)

    Particles = np.random.uniform(float(l), float(r), (int(init_population), solution_dimension))

    return Particles

def gConstant(l, iters, alpha, G0):
    Gimd = np.exp(-alpha * float(l) / iters)
    G = G0 * Gimd
    return G

def init(params):

    if 'init_pop' in params:
        init_pop = params['init_pop']
        if(init_pop<2):
            raise KeyError('Sufficient Initial Population required.')
    else:
        raise KeyError('init_pop parameter is required.')

    if 'sol_dim' in params:
        d = params['sol_dim'][1]
        k = params['sol_dim'][0]
    else:
        raise KeyError('sol_dim parameter is required.')

    if 'seed' in params:
        seed_particle = params['seed']
    else:
        seed_particle=np.random.randint(10000)

    if 'no_of_iter' in params:
        no_iteration = params['no_of_iter']
    else:
        no_iteration = params['no_of_iter']

    if 'G0' in params:
        G = params['G0']
    else:
        G=1

    if 'rj' in params:
        rj = params['rj']
    else:
        rj=np.random()

    if 'epsilon' in params:
        epsilon = params['epsilon']
    else:
        epsilon=0.001

    if 'alpha' in params:
        alpha = params['alpha']
    else:
        alpha = 10

    if 'ri' in params:
        ri=params['ri']
    else:
        ri=np.random()
    if 'type' in params:
        type=params['type']
    else:
        raise KeyError('type parameter is required.')
    cust=False
    if 'Data'not in params:
        raise KeyError('Parameter Data is required')
    if 'custom' in params:
        if 'Data' in params:
            custom=params['custom']
            Data=params['Data']
            solution_range=params['sol_range']
            cust=True
        else:
            raise AssertionError('Data List should be given for custom comparator')
    else:
        Points=params['Data'][0]
        Labels=params['Data'][1]
        if Points.shape[1] != d:
            raise KeyError('Incorrect key d ')
        if Labels.shape[0] != Points.shape[0]:
            raise AssertionError('Label and Points shape does not match')
        cust=False
    if 'custom_solution' in params:
        custom_solution=params['custom_solution']
        if len(custom_solution)!=init_pop or len(custom_solution)==0 :
            raise KeyError('Too less Initial Population')
        if custom_solution.shape[1]!=d*k :
            raise AssertionError('Size Mismatch of custom solution and dimensions')
        Particles = custom_solution
    else:
        Particles = Generate_Solutions(solution_range, init_pop,d*k,seed_particle)

    Solution = np.array((1,d*k), dtype=np.float64)
    vel = np.zeros(shape=(init_pop,d*k), dtype=np.float64)
    if(type=='min'):
        minFitness =np.finfo(np.float64).max
    else:
        minFitness=0

    for i in range(no_iteration):
        if cust==True:
            Total_fitness = FitnessAll(Particles,Data,custom,d,k)
        else:
            Total_fitness = Fitness_for_All(Particles,Labels,Points)
        #print(Total_fitness)
        Masses = Mass(Particles,Total_fitness,type,epsilon)

        Acc = acc(Particles, Masses, rj, G, i,epsilon)

        vel = velocity(vel, Acc,ri)

        Particles = Update(Particles, vel)

        if(type=='min'):
            if (min(Total_fitness) < minFitness):
                for i in range(len(Total_fitness)):
                    if (Total_fitness[i] < minFitness):
                        minFitness = Total_fitness[i]
                        Solution = Particles[i, :]
        else:
            if (max(Total_fitness) > minFitness):
                for i in range(len(Total_fitness)):
                    if (Total_fitness[i] > minFitness):
                        minFitness = Total_fitness[i]
                        Solution = Particles[i, :]

        G = gConstant(i,no_iteration,alpha,G)

    Solution.resize((d, k))
    return Solution