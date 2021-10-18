from flow import makePlayers, order_and_draw, initialize
from guiboard import GuiBoard
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class StartGameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UiComponents()
        self.show()
        self.bag, self.brd, self.letter_bonus_board, self.word_bonus_board = initialize()

    def UiComponents(self):
        self.layout = QVBoxLayout()
        self.sel_num = QLabel("Select number of players")
        self.num_pl_options = ["2", "3", "4"]
        self.num_pl = QComboBox()
        self.num_pl.addItems(self.num_pl_options)
        self.cont = QPushButton("Continue", self)
        self.cont.clicked.connect(self.buttonAction)
        self.layout.addWidget(self.sel_num, 0)
        self.layout.addWidget(self.num_pl)
        self.layout.addWidget(self.cont)
        self.setLayout(self.layout)

    def buttonAction(self):
        self.number_of_players = int(self.num_pl_options[self.num_pl.currentIndex()])
        self.sel_num.deleteLater()
        self.num_pl.deleteLater()
        self.cont.deleteLater()
        self.sublayouts = [QHBoxLayout() for ii in range(self.number_of_players)]
        self.names_input = [QLineEdit() for ii in range(self.number_of_players)]
        for ii in range(self.number_of_players):
            self.sublayouts[ii].addWidget(QLabel("Player " + str(ii+1) + ": "))
            self.sublayouts[ii].addWidget(self.names_input[ii])
            self.layout.addLayout(self.sublayouts[ii])
        self.make_pl = QPushButton("Start game")
        self.make_pl.clicked.connect(self.call_makePlayers)
        self.layout.addWidget(self.make_pl)

    def call_makePlayers(self):
        names_strings = []
        for ii in range(self.number_of_players):
            names_strings.append(self.names_input[ii].text())
        self.p_list = makePlayers(self.number_of_players, names_strings)
        order_and_draw(self.p_list, self.bag)
        for s in self.sublayouts:
            for i in reversed(range(s.count())):
                s.itemAt(i).widget().deleteLater()
            s.deleteLater()
        self.make_pl.deleteLater()
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        #self.b = GuiBoard(self.grid, self.brd, self.letter_bonus_board, self.word_bonus_board)  #fixme issue here


    def makeGuiBoard(self, grid, brd, bonus_letter, bonus_word):
        self.squares = []
        for ii in range(5):
            for jj in range(5):
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


app = QApplication([])
app.setStyle('Fusion')
window = StartGameWindow()
app.exec_()
