from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

from src.empty_screen import EmptyScreen
from src.end_screen import EndScreen
from src.game_screen import GameScreen
from src.label_grid import LabelGrid
from src.setup_screen import SetupScreen
from src.special import constants
from src.start_screen import StartScreen
from src.special.tile_state import TileState
from src.button_grid import ButtonGrid


class Application:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.window.setGeometry(100, 100, 800, 800)

        self.players_boards = [[[TileState.EMPTY for _ in range(constants.BOARD_WIDTH)] for _ in range(constants.BOARD_HEIGHT)] for _ in range(2)]
        self.button_grid = ButtonGrid(self.window)

        self.start_screen = StartScreen(self, hidden=True)
        self.setup_screen = SetupScreen(self, self.players_boards, self.button_grid, hidden=True)
        self.game_screen = GameScreen(self, self.players_boards, self.button_grid, hidden=True)
        self.empty_screen = EmptyScreen(self, self.button_grid, hidden=True)
        self.end_screen = EndScreen(self, hidden=True)

    def run(self):
        self.window.show()
        self.start_screen.show()
        sys.exit(self.app.exec())

    def reset_vars(self):
        self.players_boards = [[[TileState.EMPTY for _ in range(constants.BOARD_WIDTH)] for _ in range(constants.BOARD_HEIGHT)] for _ in range(2)]
        self.setup_screen.setup_vars(self.players_boards)
        self.game_screen.setup_vars(self.players_boards)
