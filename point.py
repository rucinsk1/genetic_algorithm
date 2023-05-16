from __future__ import annotations
import random
from math import sqrt


class Point:

    def __init__(self, id : int, x : float, y : float, start_time : int, end_time : int) -> None:
        self.id=id
        self.x=x
        self.y=y
        self.start_time=start_time
        self.end_time=end_time

    def distance(self, other : Point) -> float:
    
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

def generate_points(n_points : int, range : int = 20) -> list[Point]:
    points = []

    for i in range(n_points):
        x = random(0, range)
        y = random(0, range)
        start_time = random.randint(0, 23)
        end_time = random.randint(start_time, 24)
        points.append(Point(i, x, y, start_time, end_time))
    
    return points


        