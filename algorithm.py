
import random
from typing import Optional

from genotype import Representant
from point import generate_points

class GeneticAlgorithm:

    def __init__(self, population_size : int, iterations : int, min_value : Optional[float], n_points : int = 6, area_size : int = 20, mutation_probability : float = 0.02):
        
        self.n_points = n_points
        #self.population_size = population_size
        #self.area_size = area_size
        self.iterations = iterations
        self.min_value = min_value
        self.mutation_probability = mutation_probability
        self.population = _generate_population(population_size, area_size, n_points)




def _generate_population(population_size : int, are_size : int, n_points : int) -> list[Representant]:
    
    points = generate_points(n_points=n_points, range=are_size)
    population = []
    for _ in len(population_size):
        population.append(random.shuffle(points))
    
    return population