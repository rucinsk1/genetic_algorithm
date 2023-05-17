from __future__ import annotations
import random

from point import Point

class Representant:

    def __init__(self, genes : list[Point]) -> None:
        self.genes = genes
        self.fitness = 0

    def update_fitness(self) -> None:
        
        fitness = 0
        
        current_time = self.genes[0].start_time
        for current_point, next_point in zip(self.genes[::1], self.genes[1::1]):

            # current_point = self.genes[i]
            # next_point = self.genes[i+1] % len(self.genes) #avoid reaching not existing point

            # if i == 0:
            #     current_time = current_point.start_time

            #How long do we have to wait?
            wait_time = _time_till_open(current_time, current_point.start_time, current_point.end_time)

            #Travel distance/time
            distance = current_point.distance(next_point) 

            #update time with wait and traveling time/distance
            current_time += wait_time + distance
            current_time = current_time % 24 # day doesnt last 26 days and so on
            #update fitness (like time)
            fitness += wait_time + distance

        self.fitness = fitness
    
    def crossover(self, other : Representant) -> tuple[Representant, Representant]:

        size = len(self.genes)
        
        #random points to cross
        crossover_1 = random.randint(0, size-1)
        crossover_2 = random.randint(0, size-1)

        #choose smaller/bigger index
        start_index = min(crossover_1, crossover_2)
        end_index = max(crossover_1, crossover_2)

        #init children's genes
        child1_genes = self.genes[:]
        child2_genes = other.genes[:]

        #switch genes
        child1_genes[start_index:end_index] = other.genes[start_index:end_index]
        child2_genes[start_index:end_index] = self.genes[start_index:end_index]

        #genes should be unique
        child1_genes = list(set(child1_genes))
        child2_genes = list(set(child2_genes))

        #fix child1
        while len(child1_genes) < size:
            missing_genes = list(set(self.genes) - set(child1_genes))
            random_gene = random.choice(missing_genes)
            child1_genes.append(random_gene) #add random mssing gene
        
        #fix child2
        while len(child2_genes) < size:
            missing_genes = list(set(self.genes) - set(child2_genes))
            random_gene = random.choice(missing_genes)
            child2_genes.append(random_gene) #add random mssing gene
        
        return Representant(child1_genes), Representant(child2_genes)

    def mutate(self) -> Representant:
        index1 = random.randint(0, len(self.genes) - 1)
        index2 = random.randint(0, len(self.genes) - 1)

        self.genes[index1], self.genes[index2] = self.genes[index2], self.genes[index1]

def _time_till_open(current_time : int, start_time : int, end_time : int) -> int:
    if start_time <= current_time <= end_time:
        return 0
    elif current_time < start_time:
        return start_time - current_time
    else:
        return 24 - current_time + start_time