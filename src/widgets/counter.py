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
        for i, (background_label, counter_label, label_row) in enumerate(zip(self.background_labels, self.counter_labels, self.labels)):
            background_label.setGeometry(ax-1, ay-1 + 35*(constants.SHIP_TYPES_COUNT-i-1), 30*(i+1)+1, 31)
            background_label.setStyleSheet("background-color : black")

            counter_label.setGeometry(ax+30*(i+1)+10, ay-1 + 35*(constants.SHIP_TYPES_COUNT-i-1), 30*(i+1)+1, 31)
            for j, label in enumerate(label_row):
                label.setGeometry(ax + 30*j, ay + 35*(constants.SHIP_TYPES_COUNT-i-1), 29, 29)
                label.setStyleSheet("background-color : yellow")

    def show(self):
        for background_label, counter_label, label_row in zip(self.background_labels, self.counter_labels, self.labels):
            background_label.show()
            counter_label.show()
            for label in label_row:
                label.show()

    def hide(self):
        for background_label, counter_label, label_row in zip(self.background_labels, self.counter_labels, self.labels):
            background_label.hide()
            counter_label.hide()
            for label in label_row:
                label.hide()

    def set_position(self, ax, ay):
        for i, (background_label, counter_label, label_row) in enumerate(zip(self.background_labels, self.counter_labels, self.labels)):
            background_label.move(ax-1, ay-1 + 35*(constants.SHIP_TYPES_COUNT-i-1))
            counter_label.move(ax+30*(i+1)+10, ay-1 + 35*(constants.SHIP_TYPES_COUNT-i-1))
            for j, label in enumerate(label_row):
                label.move(ax + 30*j + 1, ay + 50*(constants.SHIP_TYPES_COUNT-i+1) + 1)

    def set_counts(self, ships):
        for i, counter_label in enumerate(self.counter_labels):
            counter_label.setText(f"x {ships[i+1]}")
