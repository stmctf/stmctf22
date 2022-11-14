from genetic_algorithm import GeneticAlgorithm
import cv2
import create_puzzle
import time


start_time = time.perf_counter()


# Change generation and population number here
GENERATIONS = 30
POPULATION = 300

# Puzzled image input.
image = cv2.imread(create_puzzle.puzzled_image_out)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Same size when creating the puzzle.
# Must be the same otherwise the program malfunctions.
piece_size = create_puzzle.piece_size

# Puzzled image output.
solution = GeneticAlgorithm(image, piece_size, POPULATION, GENERATIONS).start_evolution().to_image()

# Saving the output.
image_output = "images/output_solution/solution.jpg"
cv2.imwrite(image_output, solution)
print("Saved to '{}'".format(image_output))


finish_time = time.perf_counter()

print((finish_time - start_time) / 60.0)