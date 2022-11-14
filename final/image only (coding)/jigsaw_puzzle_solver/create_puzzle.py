"""
This file takes an image as input and divides into square pieces.
Then combines all the pieces randomly.
"""

import numpy as np
import cv2
import my_image

# CHANGE PIECE SIZE HERE(bigger value = less pieces)
piece_size = 64

# CHANGE IMAGE INPUT / OUTPUT HERE
image_input1 = "images/the_starry_night-wallpaper-2560x1440.jpg"
image_input2 = "images/85.jpg"

puzzled_image_out = "images/output_puzzle/puzzeled_out.jpg"

def _create_puzzle():
    image = cv2.imread(image_input2)

    pieces, rows, columns = my_image.flatten_image(image, piece_size)

    # Shuffle pieces randomly
    np.random.shuffle(pieces)

    # Assemble all the pieces to create a puzzle
    puzzle = my_image.assemble_image(pieces, rows, columns)

    # Save puzzle image
    cv2.imwrite(puzzled_image_out, puzzle)
    print("Puzzle created with {} pieces\n".format(len(pieces)))

_create_puzzle()