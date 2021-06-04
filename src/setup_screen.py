from PyQt5.QtWidgets import QPushButton

from src.special import constants
from src.special.game_states import GameState
from src.special.tile_state import TileState
from src.special import utils


class SetupScreen:
    def __init__(self, application, players_boards, button_grid, counter, hidden=True):
        self.app = application
        self.players_boards = None
        self.players_ships = None
        self.players_ship_count = None
        self.state = None
        self.setup_vars(players_boards)

        self.__setup_ui(button_grid, counter)
        if hidden:
            self.hide()
        else:
            self.show()

    def setup_vars(self, players_boards):
        self.players_ships = [{k: v for k, v in constants.SHIP_COUNTS.items()} for _ in range(2)]
        self.players_boards = players_boards
        self.players_ship_count = [constants.SHIP_COUNT for _ in range(2)]

    def __setup_ui(self, button_grid, counter):
        self.button_grid = button_grid
        self.button_grid.add_function(GameState.PLAYER1_PREPARING, lambda i, j: self.__on_button_pressed(i, j, 0))
        self.button_grid.add_function(GameState.PLAYER2_PREPARING, lambda i, j: self.__on_button_pressed(i, j, 1))

        self.counter = counter

        self.next_button = QPushButton(self.app.window)
        self.next_button.setGeometry(550, 650, 200, 100)
        self.next_button.setText("Next")
        self.next_button.clicked.connect(self.__on_next_button_pressed)

    def show(self, state=GameState.PLAYER1_PREPARING):
        self.state = state

        self.button_grid.show(self.players_boards[GameState.get_player(state)], state)
        self.counter.show()
        self.counter.set_counts(self.players_ships[GameState.get_player(state)])
        self.next_button.show()

    def hide(self):
        self.button_grid.hide()
        self.counter.hide()
        self.next_button.hide()

    def __on_next_button_pressed(self):
        if self.players_ship_count[GameState.get_player(self.state)] == 0:
            if self.state == GameState.PLAYER1_PREPARING:
                self.show(GameState.PLAYER2_PREPARING)
            elif self.state == GameState.PLAYER2_PREPARING:
                self.hide()
                self.app.empty_screen.show(GameState.PLAYER1_PLAYING)

    def __on_button_pressed(self, i, j, player):
        added, removed = self.__check_ship_placement(i, j, player)
        if added is False:  # and removed is False:
            return

        new_ships = self.players_ships[player].copy()
        for ship in added:
            if ship not in new_ships:
                return  # would create too large ship
            new_ships[ship] -= 1
        for ship in removed:
            new_ships[ship] += 1

        if self.__check_if_there_are_too_may_ships(new_ships):
            return

        self.players_ships[player] = new_ships
        new_tile_state = TileState.opposite(self.players_boards[player][i][j])
        self.players_ship_count[GameState.get_player(self.state)] -= TileState.get_added(new_tile_state)
        self.players_boards[player][i][j] = new_tile_state
        self.button_grid.set_button_state(i, j, new_tile_state)
        self.counter.set_counts(new_ships)

    def __check_ship_placement(self, i, j, player):
        board = self.players_boards[player]
        if board[i][j] == TileState.EMPTY:
            return self.__add_ship(i, j, board)
        else:  # board[i][j] == TileState.SHIP:
            return self.__remove_ship(i, j, board)

    def __add_ship(self, i, j, board):
        # check if there are already ships on the corners (if corners exist)
        for n_i, n_j in [(i + 1, j + 1), (i + 1, j - 1), (i - 1, j - 1), (i - 1, j + 1)]:
            if utils.in_bound(n_i, n_j) and board[n_i][n_j] != TileState.EMPTY:
                return False, False  # there is a ship on any corner

        sizes = [self.__check_side(board, i, j, di, dj) for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

        if sizes[0] + sizes[1] != 0 and sizes[2] + sizes[3] != 0:
            return False, False  # would create a curved ship

        return [sum(sizes) + 1], filter(lambda x: x != 0, sizes)

    def __remove_ship(self, i, j, board):
        sizes = [self.__check_side(board, i, j, di, dj) for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        return filter(lambda x: x != 0, sizes), [sum(sizes) + 1]

    def __check_side(self, board, i, j, di, dj):
        # count how long is the ship to that side
        size = 0
        while utils.in_bound(i + size * di + di, j + size * dj + dj) and \
                board[i + size * di + di][j + size * dj + dj] == TileState.SHIP:
            size += 1
        return size

    def __check_if_there_are_too_may_ships(self, new_ships):
        ssum = 0
        for k in range(constants.LARGEST, constants.SMALLEST - 1, -1):
            ssum += new_ships[k]
            if ssum < 0:
                return True
        return False
