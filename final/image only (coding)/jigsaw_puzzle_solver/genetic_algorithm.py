"""
This file is the combination of other files (except create_puzzle.py).
Together they make the algorithm itself.
"""

from operator import attrgetter
from selection import fitness_select
from individual import Individual
from crossover import Crossover
import my_image
import cv2


class GeneticAlgorithm(object):
    # If there is no change for # generations, terminate.
    TERMINATION_THRESHOLD = 20

    def __init__(self, image, piece_size, population_size, generations, elite_size=2):
        self._image = image
        self._piece_size = piece_size
        self._generations = generations
        self._elite_size = elite_size
        pieces, rows, columns = my_image.flatten_image(image, piece_size, indexed=True)
        self._population = [Individual(pieces, rows, columns) for _ in range(population_size)]
        self._pieces = pieces

    def start_evolution(self):
        print("Pieces:\t{}\n".format(len(self._pieces)))

        my_image.ImageAnalysis.analyze_image(self._pieces)

        fittest = None # Best individual of a generation
        best_fitness_score = float("-inf")
        termination_counter = 0
        myNum = 1

        for generation in range(self._generations):

            new_population = []

            elite = self._get_best_individuals(elites=self._elite_size)
            new_population.extend(elite)

            selected_parents = fitness_select(self._population, elites=self._elite_size)

            for first_parent, second_parent in selected_parents:
                crossover = Crossover(first_parent, second_parent)
                crossover.run()
                child = crossover.child()
                new_population.append(child)

            fittest = self._best_individual()

            if fittest.fitness <= best_fitness_score:
                termination_counter += 1
            else:
                best_fitness_score = fittest.fitness

            if termination_counter == self.TERMINATION_THRESHOLD:
                print("\nTERMINATED")
                print("There was no improvement for {} generations".format(self.TERMINATION_THRESHOLD))
                return fittest

            self._population = new_population

            # This saves the best individual of every generation. Change the path here.
            numStr = str(myNum)
            image_out = "images/output_solution/gen" + numStr + ".jpg"
            cv2.imwrite(image_out, fittest.to_image())
            myNum = myNum + 1

        return fittest

    def _get_best_individuals(self, elites):
        return sorted(self._population, key=attrgetter("fitness"))[-elites:]

    def _best_individual(self):
        return max(self._population, key=attrgetter("fitness"))