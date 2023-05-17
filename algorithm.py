
import random
from typing import Optional

from genotype import Representant
from point import generate_points

class GeneticAlgorithm:

    def __init__(self, population_size : int, iterations : int, min_value : Optional[float], n_points : int = 6, area_size : int = 20, mutation_probability : float = 0.02):
        
        self._check_args(population_size, iterations, n_points, area_size, mutation_probability)
        self.n_points = n_points
        #self.population_size = population_size
        #self.area_size = area_size
        self.iterations = iterations
        self.min_value = min_value
        self.mutation_probability = mutation_probability
        self.population = _generate_population(population_size, area_size, n_points)
        self.best = None


    def run(self):

        for i in range(self.iterations):
            for representant in self.population:
                representant.update_fitness()
            

            self.population.sort(key=lambda x:x.fitness)

            #check if best represntant of current population is the best 
            self.update_best(self.population[0], i)


            #pair best with best and worst with worst
            for parent1, parent2 in zip(self.population[::2], self.population[1::2]):
                child1, child2 = parent1.crossover(parent2)
                self.population.append(child1)
                self.population.append(child2)
            
            #mutate
            for r in self.population[1:]: #Dont wanna mutate best representant
                if random.random() <= self.mutation_probability:
                    r.mutate()
            
            #keep best representants
            self.tournament()


    def update_best(self, candidate : Representant, iteration : int) -> None:
        if self.best is None:
            self.best = candidate
            print("starting best", self.best.fitness)
        elif candidate.fitness < self.best.fitness:
            self.best = candidate
            print("Iteration:", iteration, "New best:", self.best.fitness)
            print("Best order", [x.id for x in self.best.genes])

    def tournament(self) -> None:
        random_order = self.population.copy()
        random.shuffle(random_order)
        new_population = []

        for first, second in zip(random_order[::2], random_order[1::2]):
            if first.fitness > second.fitness:
                new_population.append(first)
            else:
                new_population.append(second)

        self.population = new_population
        #print("BEST at end:", self.best.fitness)

    def _check_args(self, population_size : int, iterations : int, n_points, area_size : int, mutation_probability : float) -> None:
        if type(population_size) != int or population_size <= 0:
            raise ValueError("Invalid population_size, it should be positive integer")
        elif type(iterations) != int or iterations <= 0:
            raise ValueError("Invalid iterations, it should be positive integer")
        elif type(n_points) != int or n_points <= 0:
            raise ValueError("Invalid n_points, it should be positive integer")
        elif type(area_size) != int or area_size <= 0:
            raise ValueError("Invalid area_size, it should be positive integer")
        elif type(mutation_probability) != float or mutation_probability <= 0 or mutation_probability > 1:
            raise ValueError("Invalid mutation_probability, it should be float between 0 and 1")

def _generate_population(population_size : int, area_size : int, n_points : int) -> list[Representant]:
    
    points = generate_points(n_points=n_points, area_size=area_size)

    print("####POINTS##########")
    for p in points:
        print(p)
    print("####################")
    population = []
    for _ in range(population_size):
        genes = points.copy()
        random.shuffle(genes)
        population.append(Representant(genes))
    
    return population

