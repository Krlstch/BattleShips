from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from src.empty_screen import EmptyScreen
from src.end_screen import EndScreen
from src.game_screen import GameScreen
from src.setup_screen import SetupScreen
from src.start_screen import StartScreen
from src.tile_state import TileState
from src.button_grid import ButtonGrid


class Application:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.window.setGeometry(100, 100, 800, 800)

        players_boards = [[[TileState.EMPTY for _ in range(10)] for _ in range(10)] for _ in range(2)]
        button_grid = ButtonGrid(self.window)

        self.start_screen = StartScreen(self, hidden=False)
        self.setup_screen = SetupScreen(self, players_boards, button_grid, hidden=True)
        self.game_screen = GameScreen(self, hidden=True)
        self.empty_screen = EmptyScreen(self, hidden=True)
        self.end_screen = EndScreen(self, hidden=True)

        self.window.show()
        sys.exit(self.app.exec())
