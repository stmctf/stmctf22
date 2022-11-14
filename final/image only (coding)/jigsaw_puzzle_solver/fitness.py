"""
This file calculates the color difference between all the edges vertically and horizontally.
edge = edge of the square pieces.
"""

import numpy as np

def difference_measure(first_piece, second_piece, orientation="LR"):
    rows, columns, _ = first_piece.shape()
    color_difference = None

    # HORIZONTAL (LEFT - RIGHT)
    if orientation == "LR":
        color_difference = first_piece[:rows, columns - 1, :] - second_piece[:rows, 0, :]

    # VERTICAL (TOP - DOWN)
    if orientation == "TD":
        color_difference = first_piece[rows - 1, :columns, :] - second_piece[0, :columns, :]

    squared_color_difference = np.power(color_difference / 255.0, 2)
    color_difference_per_row = np.sum(squared_color_difference, axis=1)
    total_difference = np.sum(color_difference_per_row, axis=0)

    value = np.sqrt(total_difference)

    return value