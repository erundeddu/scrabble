from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class GuiBoard(QWidget):
    def __init__(self, grid, brd, bonus_letter, bonus_word):
        self.squares = []
        for ii in range(len(brd)):
            for jj in range(len(brd)):
                if bonus_letter[ii][jj] == 2:
                    square = Qt.red
                elif bonus_letter[ii][jj] == 3:
                    square = Qt.darkRed
                elif bonus_word[ii][jj] == 2:
                    square = Qt.white
                elif bonus_word[ii][jj] == 3:
                    square = Qt.black
                else:
                    square = Qt.lightGray
                self.squares.append(square)
                grid.addWidget(square, ii, jj)
