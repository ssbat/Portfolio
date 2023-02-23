from constante import *
import copy

class Piece:

    def __init__(self, val, size, list):
        self.val = val
        self.size = size
        self.list = list

        # ref = coordo de la case la plus en haut à gauche de la matrice de la pièce
        # (0, 0) lorsque la piece n'est pas dans grid
        self.ref = self.mini_size_piece()

    def width_length_piece(self):  # retourne la largeur et hauteur

        # En supposant que la pièce ait un référentiel (0, 0)

        max_width = 0
        max_height = 0

        min_width = 0
        min_height = 0

        for i in self.list:

            (l, c) = i

            if l > max_height:
                max_height = l

            elif l < min_height:
                min_height = l

            if c > max_width:
                max_width = c

            elif c < min_width:
                min_width = c

        return max_height - min_height + 1, max_width - min_width + 1

    def rotation_piece(self):

        for i in range(len(self.list)):
            (l, c) = self.list[i]

            self.list[i] = (c, -l)

        # for coordo in self.list:
            # print(coordo)

    def mini_size_piece(self): # retourne le coin en haut à gauche de la pièce

        min_l, min_c = (100, 100)

        for i in self.list:

            (l, c) = i

            if l < min_l:
                min_l = l

            if c < min_c:
                min_c = c

        return min_l, min_c

    def piece_to_ref(self): # translatte la pièce de sorte que le coté haut gauche soit (0, 0)

        (l, c) = self.mini_size_piece()

        for i in range(len(self.list)):

            coordo = self.list[i]

            self.list[i] = coordo[0] - l, coordo[1] - c

        self.ref = self.mini_size_piece()

    def can_place(self, grid, position):

        (ref_l, ref_c) = position
        case_list = []

        for i in range(len(self.list)):

            (l, c) = self.list[i]

            l += ref_l
            c += ref_c

            if 0 <= l < NB_LINE and 0 <= c < NB_COLUMN and grid[l][c] == VIDE:
                case_list.append((l, c))
            else:
                return False

        return case_list

    def place_piece(self, grid, position):

        case_list = self.can_place(grid, position)

        if case_list != False:

            for coord in case_list:
                (l, c) = coord
                grid[l][c] = self.val

            return True
        return False

    def redundancy_in_rotation(self):

        last_p = copy.deepcopy(Piece(self.val, self.size, self.list))

        last_p.rotation_piece()
        last_p.piece_to_ref()

        print(self.list)
        print(last_p.list)

        if self.are_same_piece(last_p):
            return 1

        last_p.rotation_piece()
        last_p.piece_to_ref()

        if self.are_same_piece(last_p):
            return 2

        return 4

    def are_same_piece(self, piece):

        for i in piece.list:

            (l, c) = i

            if not self.is_in_piece(l, c):
                return False

        return True

    def is_in_piece(self, l, c):

        for i in self.list:
            (l_2, c_2) = i

            if l_2 == l and c_2 == c:
                return True

        return False














