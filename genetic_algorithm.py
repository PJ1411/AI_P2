from random import randrange
from n_queens_problem import *

def getRandomPop(size):
    pop = []
    for i in range(0,size):
        state = []
        for k in range(0,8):
            n = randrange(8)
            state.insert(k,n);
        pop.insert(i,state);

    return pop;
            
    

def fitness(state):
    fit = 28;
    for i in range(0,8):
        for x in range(i+1,8):
            ###check row##
            if(state[i]==state[x]):
                fit -= 1;
            ###check diagonal fields##
            if(state[i]<state[x]):
                if((x-i)+state[i]==state[x]):
                    fit -= 1;
            if(state[i]>state[x]):
                if(state[i]-(x-i)==state[x]):
                    fit -= 1;
    return fit;

def set_population(pop):
    temp_pop =[];
    for i in range(0,len(pop)):
        fit = fitness(pop[i]);
        if(fit>23):
            temp_pop.insert(len(temp_pop),pop[i]);
            temp_pop.insert(len(temp_pop),pop[i]);
            temp_pop.insert(len(temp_pop),pop[i]);
        elif(fit>17):
            temp_pop.insert(len(temp_pop),pop[i]);
            temp_pop.insert(len(temp_pop),pop[i]);
        else:
            temp_pop.insert(len(temp_pop),pop[i]);
    return temp_pop;
                  
                
def random_selection(pop):
    rand_zahl = randrange(len(pop))
    return pop[rand_zahl];

def reproduce(x,y):
    n = len(x);
    c = randrange(n);
    x_neu =[]
    y_neu =[]
    for i in range(0,c):
        x_neu.insert(len(x_neu),x[i]);
    for i in range(c,n):
        y_neu.insert(len(y_neu),y[i]);
    return x_neu +y_neu

def mutate(child):
    i = randrange(len(child))
    k = randrange(8)
    child[i] = k;
    return child;

def getBestState(population):
    bestState = population[0]
    for i in range(0,len(population)):
        if(fitness(bestState)<fitness(population[i])):
           bestState = population[i];
    return bestState;
        


def Genetic_Algorithm_print(population):
    iteration = 0;
    while iteration <100:
        new_pop = [];
        set_pop = set_population(population);
        for i in range(0,len(population)):
            x = random_selection(set_pop)
            y = random_selection(set_pop)
            child = reproduce(x,y)
            if(randrange(100)<3):
                child = mutate(child);
            new_pop.insert(len(new_pop),child);
            if(fitness(child)==28):
                print("Found solution!");
                print("Iteration: ", iteration)
                board = queens_problem(child);
                print("heuristic-cost: ",board.heuristic());
                board.draw()
                return
        population = new_pop;
        print("Iteration: ", iteration)
        state = getBestState(population)
        board = queens_problem(state);
        print("heuristic-cost: ",board.heuristic());
        board.draw()
        iteration +=1;
    state = getBestState(population)
    print("Best state after 100 iterations");
    print(state);
    print("Fitness: ",fitness(state));
    return

def Genetic_Algorithm(population):
    iteration = 0;
    while iteration <100:
        new_pop = [];
        set_pop = set_population(population);
        for i in range(0,len(population)):
            x = random_selection(set_pop)
            y = random_selection(set_pop)
            child = reproduce(x,y)
            if(randrange(100)<3):
                child = mutate(child);
            new_pop.insert(len(new_pop),child);
            if(fitness(child)==28):
                print("Found solution!");
                print("Iteration: ", iteration)
                print(child)
                return
        population = new_pop;
        iteration +=1;
    state = getBestState(population)
    print("Best state after 100 iterations");
    print(state);
    print("Fitness: ",fitness(state));
    return


###########Tests####################
starting_pop = randrange(10,100);
print("Starting population: ", starting_pop)
pop = getRandomPop(starting_pop);
Genetic_Algorithm_print(pop);
