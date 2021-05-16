from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

from src.label_grid import LabelGrid
from src.special import constants
from src.special.game_states import GameState
from src.special.tile_state import TileState


class GameScreen:
    def __init__(self, application, players_boards, button_grid, hidden=True):
        self.app = application

        self.players_boards = None
        self.won = None
        self.state = None
        self.players_ships = None
        self.selected_tile = None
        self.already_shot = None
        self.setup_vars(players_boards)

        self.setup_ui(button_grid)
        if hidden:
            self.hide()
        else:
            self.show()

    def setup_vars(self, players_boards):
        self.won = False
        self.players_ships = [constants.SHIP_COUNT, constants.SHIP_COUNT]
        self.players_boards = players_boards

    def setup_ui(self, button_grid):
        self.button_grid = button_grid
        self.button_grid.add_function(GameState.PLAYER1_PLAYING, lambda i, j: self.button_pressed(i, j, 1))
        self.button_grid.add_function(GameState.PLAYER2_PLAYING, lambda i, j: self.button_pressed(i, j, 0))

        self.label_grid = LabelGrid(self.app.window, ax=50, ay=450)

        self.next_button = QPushButton(self.app.window)
        self.next_button.setGeometry(550, 650, 200, 100)
        self.next_button.setText("Shoot")
        # self.next_button.setFont(QFont("Arial Font", 20))
        self.next_button.clicked.connect(self.__on_next_button_pressed)

    def show(self, state=GameState.PLAYER1_PLAYING):
        self.state = state
        board = self.players_boards[GameState.get_player(state)]
        opponent_board = self.players_boards[GameState.get_opposite_player(state)]

        self.button_grid.show(opponent_board, state)
        self.label_grid.show(board, GameState.opposite(state))
        self.next_button.setText("Shoot")
        self.next_button.show()

        self.already_shot = False

    def hide(self):
        self.button_grid.hide()
        self.label_grid.hide()
        self.next_button.hide()

    def button_pressed(self, i, j, player):
        if not self.already_shot:
            board = self.players_boards[player]

            if not TileState.is_shot(board[i][j]):
                if self.selected_tile is not None:
                    s_i, s_j = self.selected_tile
                    self.button_grid.set_button_state(s_i, s_j, board[s_i][s_j])
                self.button_grid.set_selected(i, j)
                self.selected_tile = (i, j)

    def __on_next_button_pressed(self):
        if not self.already_shot:
            if self.selected_tile is not None:
                s_i, s_j = self.selected_tile
                board = self.players_boards[GameState.get_opposite_player(self.state)]
                new_tile_state = TileState.shoot(board[s_i][s_j])
                board[s_i][s_j] = new_tile_state
                self.button_grid.set_button_state(s_i, s_j, board[s_i][s_j])
                self.selected_tile = None
                if new_tile_state == TileState.EMPTY_SHOT: # missed
                    self.already_shot = True
                    self.next_button.setText("Next")
                else:  # hit
                    self.players_ships[GameState.get_opposite_player(self.state)] -= 1
                    if self.players_ships[GameState.get_opposite_player(self.state)] == 0: # if destroyed all ships
                        self.won = True
                        self.already_shot = True
                        self.next_button.setText("Next")

        else:  #self.already_shot:
            self.hide()
            if not self.won:
                self.app.empty_screen.show(GameState.opposite(self.state))
            else:
                self.app.end_screen.show(self.state)
