from PyQt5.QtWidgets import QPushButton, QLabel
from src.special import constants
from src.special.game_states import GameState
from src.special.tile_state import TileState


class ButtonGrid:
    def __init__(self, parent, ax=0, ay=0):
        self.parent = parent
        self.state = None
        self.functions = {}

        self.background_label = QLabel(self.parent)
        self.background_label.setGeometry(ax-2, ay-2, 30*constants.BOARD_WIDTH+3, 30*constants.BOARD_WIDTH+3)
        self.background_label.setStyleSheet("background-color: black")

        self.buttons = [[QPushButton(self.parent) for j in range(constants.BOARD_HEIGHT)] for i in range(constants.BOARD_WIDTH)]
        for i, button_row in enumerate(self.buttons):
            for j, button in enumerate(button_row):
                button.setGeometry(ax+30*j, ay+30*i, 29, 29)
                button.clicked.connect(lambda checked, arg=(i, j): self.__on_button_pressed(arg[0], arg[1]))

    def __on_button_pressed(self, i, j):
        self.functions[self.state](i, j)

    def add_function(self, state, func):
        self.functions[state] = func

    def show(self, board, state):
        self.set_state(state)
        self.background_label.show()
        for i, button_row in enumerate(self.buttons):
            for j, button in enumerate(button_row):
                self.set_button_state(i, j, board[i][j])
                button.show()

    def hide(self):
        self.background_label.hide()
        for button_row in self.buttons:
            for button in button_row:
                button.hide()

    def set_position(self, ax, ay):
        self.background_label.move(ax-2, ay-2)
        for i, button_row in enumerate(self.buttons):
            for j, button in enumerate(button_row):
                button.move(ax+30*j, ay+30*i)

    def set_button_state(self, i, j, tile_state):
        button = self.buttons[i][j]
        if tile_state == TileState.EMPTY:
            button.setStyleSheet("background-color : gray")
            button.setText("")
        elif tile_state == TileState.SHIP:
            if GameState.is_preparing(self.state):
                button.setStyleSheet("background-color : yellow")
                button.setText("")
            else:  # GameState.is_preparing(self.playing):
                button.setStyleSheet("background-color : gray")
                button.setText("")
        elif tile_state == TileState.EMPTY_SHOT:
            button.setStyleSheet("background-color : gray")
            button.setText("X")
        elif tile_state == TileState.SHIP_SHOT:
            button.setStyleSheet("background-color : yellow")
            button.setText("X")

    def set_selected(self, i, j):
        self.buttons[i][j].setStyleSheet("background-color : red")

    def set_state(self, state):
        if not GameState.is_same_phase(self.state, state):
            if GameState.is_preparing(state):
                self.set_position(50, 450)
            else:  # GameState.is_playing(state)
                self.set_position(50, 50)
        self.state = state
