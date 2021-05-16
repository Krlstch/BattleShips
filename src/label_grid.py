from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel
from src.special import constants
from src.special.game_states import GameState
from src.special.tile_state import TileState


class LabelGrid:
    def __init__(self, parent, ax=0, ay=0):
        self.parent = parent
        self.state = None
        self.functions = {}

        self.labels = [[QLabel(self.parent) for j in range(constants.BOARD_HEIGHT)] for i in range(
            constants.BOARD_WIDTH)]
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.labels[i][j].setGeometry(ax+30*j + 1, ay+30*i + 1, 28, 28)
                self.labels[i][j].setAlignment(Qt.AlignCenter)
                #self.labels[i][j].setStyleSheet("border: 1px solid black;")

    def show(self, board, state):
        self.set_state(state)
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.set_label_state(i, j, board[i][j])
                self.labels[i][j].show()

    def hide(self):
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.labels[i][j].hide()

    def set_position(self, ax, ay):
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.labels[i][j].setGeometry(ax+30*j + 1, ay+30*i + 1, 28, 28)

    def set_label_state(self, i, j, tile_state):
        if tile_state == TileState.EMPTY:
            self.labels[i][j].setStyleSheet("background-color : grey")
            self.labels[i][j].setText("")
        elif tile_state == TileState.SHIP:
            self.labels[i][j].setStyleSheet("background-color : yellow")
            self.labels[i][j].setText("")
        elif tile_state == TileState.EMPTY_SHOT:
            self.labels[i][j].setStyleSheet("background-color : gray")
            self.labels[i][j].setText("X")
        elif tile_state == TileState.SHIP_SHOT:
            self.labels[i][j].setStyleSheet("background-color : yellow")
            self.labels[i][j].setText("X")

    def set_state(self, state):
        self.state = state
