from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel
from src.special import constants
from src.special.game_states import GameState
from src.special.tile_state import TileState


class LabelGrid:
    def __init__(self, parent, ax=0, ay=0):
        self.parent = parent
        self.state = None

        self.background_label = QLabel(self.parent)
        self.background_label.setGeometry(ax-1, ay-1, 303, 303)
        self.background_label.setStyleSheet("background-color: black")

        self.labels = [[QLabel(self.parent) for j in range(constants.BOARD_HEIGHT)] for _ in range(constants.BOARD_WIDTH)]
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.labels[i][j].setGeometry(ax+30*j + 1, ay+30*i + 1, 29, 29)
                self.labels[i][j].setAlignment(Qt.AlignCenter)

    def show(self, board, state):
        self.set_state(state)
        self.background_label.show()
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.set_label_state(i, j, board[i][j])
                self.labels[i][j].show()

    def hide(self):
        self.background_label.hide()
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.labels[i][j].hide()

    def set_position(self, ax, ay):
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.labels[i][j].move(ax+30*j + 1, ay+30*i + 1)

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
