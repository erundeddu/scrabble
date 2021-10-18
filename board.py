class Board:

    def __init__(self):
        self.brd = [[None for ii in range(17)] for jj in range(17)]

    def get_letter(self, pos):
        row, col = pos
        return self.brd[row][col]

    def is_free(self, pos):
        row, col = pos
        if self.brd[row][col] is None:
            return True
        else:
            return False

    def add_letter(self, let, pos):
        row, col = pos
        self.brd[row][col] = let

    def rm_letter(self, pos):
        row, col = pos
        self.brd[row][col] = None

    def __str__(self):
        brd_str = ""
        for ii in range(17):
            for jj in range(17):
                if self.brd[ii][jj] is None:
                    brd_str += ". "
                else:
                    brd_str += self.brd[ii][jj].get_char() + " "
            brd_str += "\n"
        return brd_str
