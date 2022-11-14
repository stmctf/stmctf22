"""
This file takes two individuals and exchanges some pieces
in order to increase diversity.
"""

import random
import heapq

from my_image import ImageAnalysis
from individual import Individual

SHARED_PIECE_PRIORITY = -10
BUDDY_PIECE_PRIORITY = -1


class Crossover(object):

    def __init__(self, individual1, individual2):
        self._parents = (individual1, individual2)
        self._pieces_length = len(individual1.pieces)
        self._child_rows = individual1.rows
        self._child_columns = individual1.columns

        # Borders of main(growing)
        self._min_row = 0
        self._max_row = 0
        self._min_column = 0
        self._max_column = 0

        self._main = {}
        self._taken_positions = set()

        # Priority queue
        self._candidate_pieces = []

    def child(self):
        pieces = [None] * self._pieces_length

        for piece, (row, column) in self._main.items():
            index = (row - self._min_row) * self._child_columns + (column - self._min_column)
            pieces[index] = self._parents[0].piece_by_id(piece)

        return Individual(pieces, self._child_rows, self._child_columns, shuffle=False)

    # Check piece is swapped or not, if it is find a new possible piece to add to queue
    # Add pieces to growing main
    def run(self):
        self._initialize_main()

        while len(self._candidate_pieces) > 0:
            _, (position, piece_id), relative_piece = heapq.heappop(self._candidate_pieces)

            if position in self._taken_positions:
                continue

            if piece_id in self._main:
                self.add_piece_possible(relative_piece[0], relative_piece[1], position)
                continue

            self._add_pieces_to_main(piece_id, position)

    def _initialize_main(self):
        root_piece = self._parents[0].pieces[int(random.uniform(0, self._pieces_length))]
        self._add_pieces_to_main(root_piece.id, (0, 0))

    def _add_pieces_to_main(self, piece_id, position):
        self._main[piece_id] = position
        self._taken_positions.add(position)
        self._refresh_possible_pieces(piece_id, position)

    def _refresh_possible_pieces(self, piece_id, position):
        available_boundaries = self._available_edges(position)

        for orientation, position in available_boundaries:
            self.add_piece_possible(piece_id, orientation, position)

    def add_piece_possible(self, piece_id, orientation, position):
        shared_piece = self._get_shared_piece(piece_id, orientation)
        if self._valid_piece(shared_piece):
            self._add_shared_piece_possible(shared_piece, position, (piece_id, orientation))
            return

        buddy_piece = self._get_buddy_piece(piece_id, orientation)
        if self._valid_piece(buddy_piece):
            self._add_buddy_piece_possible(buddy_piece, position, (piece_id, orientation))
            return

        best_match_piece, priority = self._get_best_match_piece(piece_id, orientation)
        if self._valid_piece(best_match_piece):
            self._add_best_match_piece_possible(best_match_piece, position, priority, (piece_id, orientation))
            return

    def _get_shared_piece(self, piece_id, orientation):
        first_parent, second_parent = self._parents
        first_parent_edge = first_parent.edge(piece_id, orientation)
        second_parent_edge = second_parent.edge(piece_id, orientation)

        if first_parent_edge == second_parent_edge:
            return first_parent_edge

    def _get_buddy_piece(self, piece_id, orientation):
        first_buddy = ImageAnalysis.best_match(piece_id, orientation)
        second_buddy = ImageAnalysis.best_match(first_buddy, complementary_orientation(orientation))

        if second_buddy == piece_id:
            for edge in [parent.edge(piece_id, orientation) for parent in self._parents]:
                if edge == first_buddy:
                    return edge

    def _get_best_match_piece(self, piece_id, orientation):
        for piece, dissimilarity_measure in ImageAnalysis.best_match_table[piece_id][orientation]:
            if self._valid_piece(piece):
                return piece, dissimilarity_measure

    def _add_shared_piece_possible(self, piece_id, position, relative_piece):
        piece_candidate = (SHARED_PIECE_PRIORITY, (position, piece_id), relative_piece)
        heapq.heappush(self._candidate_pieces, piece_candidate)

    def _add_buddy_piece_possible(self, piece_id, position, relative_piece):
        piece_candidate = (BUDDY_PIECE_PRIORITY, (position, piece_id), relative_piece)
        heapq.heappush(self._candidate_pieces, piece_candidate)

    def _add_best_match_piece_possible(self, piece_id, position, priority, relative_piece):
        piece_candidate = (priority, (position, piece_id), relative_piece)
        heapq.heappush(self._candidate_pieces, piece_candidate)

    def _available_edges(self, row_and_column):
        (row, column) = row_and_column
        edges = []

        if not self._main_full():
            positions = {
                "T": (row - 1, column),
                "R": (row, column + 1),
                "D": (row + 1, column),
                "L": (row, column - 1)
            }

            for orientation, position in positions.items():
                if position not in self._taken_positions and self._in_range(position):
                    self._refresh_main_edges(position)
                    edges.append((orientation, position))

        return edges

    def _main_full(self):
        return len(self._main) == self._pieces_length

    def _in_range(self, row_and_column):
        (row, column) = row_and_column
        return self._row_in_range(row) and self._column_in_range(column)

    def _row_in_range(self, row):
        current_rows = abs(min(self._min_row, row)) + abs(max(self._max_row, row))
        return current_rows < self._child_rows

    def _column_in_range(self, column):
        current_columns = abs(min(self._min_column, column)) + abs(max(self._max_column, column))
        return current_columns < self._child_columns

    def _refresh_main_edges(self, row_and_column):
        (row, column) = row_and_column
        self._min_row = min(self._min_row, row)
        self._max_row = max(self._max_row, row)
        self._min_column = min(self._min_column, column)
        self._max_column = max(self._max_column, column)

    def _valid_piece(self, piece_id):
        return piece_id is not None and piece_id not in self._main


def complementary_orientation(orientation):
    return {
        "T": "D",
        "R": "L",
        "D": "T",
        "L": "R"
    }.get(orientation, None)