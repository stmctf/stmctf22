"""
This file makes all the image operations.
"""

from fitness import difference_measure
import numpy as np
from piece import Piece

# Divide image into square pieces and add to a list
def flatten_image(image, piece_size, indexed=False):
    rows, columns = image.shape[0] // piece_size, image.shape[1] // piece_size
    pieces = []

    for y in range(rows):
        for x in range(columns):
            left, top, w, h = x * piece_size, y * piece_size, (x + 1) * piece_size, (y + 1) * piece_size
            piece = np.empty((piece_size, piece_size, image.shape[2]))
            piece[:piece_size, :piece_size, :] = image[top:h, left:w, :]
            pieces.append(piece)

    if indexed:
        pieces = [Piece(value, index) for index, value in enumerate(pieces)]

    return pieces, rows, columns


# Combine the pieces
def assemble_image(pieces, rows, columns):
    vertical_stack = []
    for i in range(rows):
        horizontal_stack = []
        for j in range(columns):
            horizontal_stack.append(pieces[i * columns + j])
        vertical_stack.append(np.hstack(horizontal_stack))
    return np.vstack(vertical_stack).astype(np.uint8)


# Basically storage for difference measures of individuals
class ImageAnalysis(object):
    difference_measures = {}
    best_match_table = {}

    @classmethod
    def analyze_image(cls, pieces):
        # We store the best matches as a sorted list (lower difference measure = higher priority)
        for piece in pieces:
            cls.best_match_table[piece.id] = {
                "T": [],
                "R": [],
                "D": [],
                "L": []
            }

        # Calculating difference measure and best match
        def update_best_match_table(first_piece, second_piece):
            measure = difference_measure(first_piece, second_piece, orientation)
            cls.put_difference((first_piece.id, second_piece.id), orientation, measure)
            cls.best_match_table[second_piece.id][orientation[0]].append((first_piece.id, measure))
            cls.best_match_table[first_piece.id][orientation[1]].append((second_piece.id, measure))

        iterations = len(pieces) - 1
        for first in range(iterations):
            for second in range(first + 1, len(pieces)):
                for orientation in ["LR", "TD"]:
                    update_best_match_table(pieces[first], pieces[second])
                    update_best_match_table(pieces[second], pieces[first])

        for piece in pieces:
            for orientation in ["T", "L", "R", "D"]:
                cls.best_match_table[piece.id][orientation].sort(key=lambda x: x[1])

    @classmethod
    def put_difference(cls, ids, orientation, value):
        if ids not in cls.difference_measures:
            cls.difference_measures[ids] = {}
        cls.difference_measures[ids][orientation] = value

    @classmethod
    def get_difference(cls, ids, orientation):
        return cls.difference_measures[ids][orientation]

    @classmethod
    def best_match(cls, piece, orientation):
        return cls.best_match_table[piece][orientation][0][0]