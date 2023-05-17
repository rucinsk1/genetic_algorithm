from algorithm import GeneticAlgorithm


if __name__ == "__main__":

    a = GeneticAlgorithm(
        population_size=20,
        iterations=100000,
        n_points=6,
        area_size=10,
        min_value=100
        )
    a.run()