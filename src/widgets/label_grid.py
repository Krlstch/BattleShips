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
        self.background_label.setGeometry(ax-2, ay-2, 30*constants.BOARD_WIDTH+3, 30*constants.BOARD_WIDTH+3)
        self.background_label.setStyleSheet("background-color: black")

        self.labels = [[QLabel(self.parent) for _ in range(constants.BOARD_HEIGHT)] for _ in range(constants.BOARD_WIDTH)]
        for i, label_row in enumerate(self.labels):
            for j, label in enumerate(label_row):
                label.setGeometry(ax + 30 * j, ay + 30 * i, 29, 29)
                label.setAlignment(Qt.AlignCenter)

    def show(self, board, state):
        self.state = state
        self.background_label.show()
        for i, label_row in enumerate(self.labels):
            for j, label in enumerate(label_row):
                self.set_label_state(i, j, board[i][j])
                label.show()

    def hide(self):
        self.background_label.hide()
        for label_row in self.labels:
            for label in label_row:
                label.hide()

    def set_position(self, ax, ay):
        for i, label_row in enumerate(self.labels):
            for j, label in enumerate(label_row):
                label.move(ax + 30 * j + 1, ay + 30 * i + 1)

    def set_label_state(self, i, j, tile_state):
        label = self.labels[i][j]
        if tile_state == TileState.EMPTY:
            label.setStyleSheet("background-color : grey")
            label.setText("")
        elif tile_state == TileState.SHIP:
            label.setStyleSheet("background-color : yellow")
            label.setText("")
        elif tile_state == TileState.EMPTY_SHOT:
            label.setStyleSheet("background-color : gray")
            label.setText("X")
        elif tile_state == TileState.SHIP_SHOT:
            label.setStyleSheet("background-color : yellow")
            label.setText("X")
