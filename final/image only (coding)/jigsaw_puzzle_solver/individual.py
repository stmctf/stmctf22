"""
This file is representing a solution of every member.
It is created by shuffling the pieces randomly.
"""

import numpy as np
import my_image

class Individual(object):
    FITNESS_FACTOR = 1000

    def __init__(self, pieces, rows, columns, shuffle=True):
        self.pieces = pieces[:]
        self.rows = rows
        self.columns = columns
        self._fitness = None

        if shuffle:
            np.random.shuffle(self.pieces)

        self._piece_mapping = {piece.id: index for index, piece in enumerate(self.pieces)}

    def __getitem__(self, key):
        return self.pieces[key * self.columns:(key + 1) * self.columns]

    # Calculating sum of difference measure between every adjacent pieces
    @property
    def fitness(self):
        if self._fitness is None:
            fitness_value = 1 / self.FITNESS_FACTOR

            for i in range(self.rows):
                for j in range(self.columns - 1):
                    ids = (self[i][j].id, self[i][j + 1].id)
                    fitness_value += my_image.ImageAnalysis.get_difference(ids, orientation="LR")

            for i in range(self.rows - 1):
                for j in range(self.columns):
                    ids = (self[i][j].id, self[i + 1][j].id)
                    fitness_value += my_image.ImageAnalysis.get_difference(ids, orientation="TD")

            self._fitness = self.FITNESS_FACTOR / fitness_value

        return self._fitness

    def piece_size(self):
        return self.pieces[0].size

    def piece_by_id(self, identifier):
        return self.pieces[self._piece_mapping[identifier]]

    def to_image(self):
        pieces = [piece.image for piece in self.pieces]
        return my_image.assemble_image(pieces, self.rows, self.columns)

    def edge(self, piece_id, orientation):
        edge_index = self._piece_mapping[piece_id]

        if (orientation == "T") and (edge_index >= self.columns):
            return self.pieces[edge_index - self.columns].id

        if (orientation == "R") and (edge_index % self.columns < self.columns - 1):
            return self.pieces[edge_index + 1].id

        if (orientation == "D") and (edge_index < (self.rows - 1) * self.columns):
            return self.pieces[edge_index + self.columns].id

        if (orientation == "L") and (edge_index % self.columns > 0):
            return self.pieces[edge_index - 1].id