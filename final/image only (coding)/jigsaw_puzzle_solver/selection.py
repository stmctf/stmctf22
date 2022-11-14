"""
This file selects the best individuals from the population
"""

import random
import bisect

xrange = range

# Every individual is selected proportional to its fitness score
def fitness_select(population, elites=4):
    fitness_values = [individual.fitness for individual in population]
    probability_intervals = [sum(fitness_values[:i + 1]) for i in range(len(fitness_values))]

    def select_individual():
        random_select = random.uniform(0, probability_intervals[-1])
        selected_index = bisect.bisect_left(probability_intervals, random_select)
        return population[selected_index]

    selected = []
    for i in xrange(len(population) - elites):
        first, second = select_individual(), select_individual()
        selected.append((first, second))

    return selected