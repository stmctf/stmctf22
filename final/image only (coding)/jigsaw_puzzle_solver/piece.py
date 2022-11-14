"""
This file represents a single puzzle piece.
Every piece has an identifier so they can be tracked.
"""

class Piece(object):
    def __init__(self, image, index):
        self.image = image[:]
        self.id = index

    def __getitem__(self, index):
        return self.image.__getitem__(index)

    def size(self):
        return self.image.shape[0]

    def shape(self):
        return self.image.shape