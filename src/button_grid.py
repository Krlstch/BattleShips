from PyQt5.QtWidgets import QPushButton
from src import constants


class ButtonGrid:
    def __init__(self, parent, ax=0, ay=0):
        self.parent = parent
        self.state = None
        self.functions = {}

        self.buttons = [[QPushButton(self.parent) for j in range(constants.BOARD_HEIGHT)] for i in range(constants.BOARD_WIDTH)]
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.buttons[i][j].setGeometry(ax+30*j, ay+30*i, 30, 30)
                self.buttons[i][j].clicked.connect(lambda checked, arg=(i, j): self.__on_button_pressed(arg[0], arg[1]))

    def __on_button_pressed(self, i, j):
        self.functions[self.state](i, j)

    def add_function(self, state, func):
        self.functions[state] = func

    def show(self):
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.buttons[i][j].show()

    def hide(self):
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.buttons[i][j].hide()

    def set_position(self, ax, ay):
        for i in range(constants.BOARD_WIDTH):
            for j in range(constants.BOARD_HEIGHT):
                self.buttons[i][j].setGeometry(ax+30*j, ay+30*i, 30, 30)

    def set_button_state(self, i, j, state):
        self.buttons[i][j].setStyleSheet("background-color : yellow")