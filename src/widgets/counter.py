from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel
from src.special import constants
from src.special.game_states import GameState
from src.special.tile_state import TileState


class Counter:
    def __init__(self, parent, ax=0, ay=0):
        self.parent = parent

        self.labels = [[QLabel(self.parent) for j in range(ship_size+1)] for ship_size in range(constants.SHIP_TYPES_COUNT)]
        for i in range(constants.SHIP_TYPES_COUNT):
            for j in range(i+1):
                self.labels[i][j].setGeometry(ax + 35*j + 1, ay + 35*(constants.SHIP_TYPES_COUNT-i-1) + 1, 28, 28)
                self.labels[i][j].setStyleSheet("background-color : yellow; border: 1px solid black")

    def show(self):
        for i in range(constants.SHIP_TYPES_COUNT):
            for j in range(i+1):
                self.labels[i][j].show()

    def hide(self):
        for i in range(constants.SHIP_TYPES_COUNT):
            for j in range(i+1):
                self.labels[i][j].hide()

    def set_position(self, ax, ay):
        for i in range(constants.SHIP_TYPES_COUNT):
            for j in range(i+1):
                self.labels[i][j].move(ax + 30*j + 1, ay + 50*(constants.SHIP_TYPES_COUNT-i+1) + 1)
