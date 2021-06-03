from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel
from src.special import constants
from src.special.game_states import GameState
from src.special.tile_state import TileState


class Counter:
    def __init__(self, parent, ax=0, ay=0):
        self.parent = parent

        self.background_labels = [QLabel(self.parent) for _ in range(constants.SHIP_TYPES_COUNT)]
        self.labels = [[QLabel(self.parent) for _ in range(ship_size + 1)] for ship_size in range(constants.SHIP_TYPES_COUNT)]
        self.counter_labels = [QLabel(self.parent) for _ in range(constants.SHIP_TYPES_COUNT)]
        for i in range(constants.SHIP_TYPES_COUNT):
            self.background_labels[i].setGeometry(ax-1, ay-1 + 35*(constants.SHIP_TYPES_COUNT-i-1), 30*(i+1)+1, 31)
            self.background_labels[i].setStyleSheet("background-color : black")

            self.counter_labels[i].setGeometry(ax+30*(i+1)+10, ay-1 + 35*(constants.SHIP_TYPES_COUNT-i-1), 30*(i+1)+1, 31)
            self.counter_labels[i].setText("x 0")
            for j in range(i+1):
                self.labels[i][j].setGeometry(ax + 30*j, ay + 35*(constants.SHIP_TYPES_COUNT-i-1), 29, 29)
                self.labels[i][j].setStyleSheet("background-color : yellow")

    def show(self):
        for i in range(constants.SHIP_TYPES_COUNT):
            self.background_labels[i].show()
            self.counter_labels[i].show()
            for j in range(i+1):
                self.labels[i][j].show()

    def hide(self):
        for i in range(constants.SHIP_TYPES_COUNT):
            self.background_labels[i].hide()
            self.counter_labels[i].hide()
            for j in range(i+1):
                self.labels[i][j].hide()

    def set_position(self, ax, ay):
        for i in range(constants.SHIP_TYPES_COUNT):
            self.background_labels[i].setGeometry(ax-1, ay-1 + 35*(constants.SHIP_TYPES_COUNT-i-1))
            for j in range(i+1):
                self.labels[i][j].move(ax + 30*j + 1, ay + 50*(constants.SHIP_TYPES_COUNT-i+1) + 1)
