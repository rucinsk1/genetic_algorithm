from __future__ import annotations
import random

from point import Point

class Representant:

    def __init__(self, genes : list[Point]) -> None:
        self.genes = genes
        self.fitness = 0

    def update_fitness(self) -> None:
        
        fitness = 0

        for i in range(len(self.genes)):
            current_point = self.genes[i]
            next_point = self.genes[i+1] % len(self.genes) #avoid reaching not existing point

            if i == 0:
                current_time = current_point.start_time

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
        pass

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