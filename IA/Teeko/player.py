from constante import *


class Player:

    def __init__(self, grid, token):

        self.list_pieces = []
        self.token = token

        for l in range(NB_LINE):
            for c in range(NB_COLUMN):

                if grid[l][c] == self.token:
                    self.list_pieces.append((l, c))

    def actu_list_pieces(self, grid):

        for l in range(NB_LINE):
            for c in range(NB_COLUMN):

                if grid[l][c] == self.token:
                    self.list_pieces.append((l, c))

    def vide_list_pieces(self):

        self.list_pieces = []

    def add_piece(self, piece):

        self.list_pieces.append(piece)

    def remove_piece(self, piece):

        self.list_pieces.remove(piece)










