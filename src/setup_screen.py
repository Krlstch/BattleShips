from src.button_grid import ButtonGrid
from src.game_states import GameState
from src import constants
from src.tile_state import TileState


class SetupScreen:
    def __init__(self, application, hidden=True):
        self.app = application

        self.setup_ui()
        if hidden:
            self.hide()
        else:
            self.show()

    def setup_ui(self):
        self.button_grid = ButtonGrid(self.app.window, 50, 450)
        self.button_grid.add_function(GameState.PLAYER1_PREPARING, lambda i, j: self.button_pressed(i, j, 0))
        self.button_grid.add_function(GameState.PLAYER2_PREPARING, lambda i, j: self.button_pressed(i, j, 1))

    def show(self, state=GameState.PLAYER1_PREPARING):
        self.button_grid.state = state
        self.button_grid.show()

    def hide(self):
        self.button_grid.hide()

    def button_pressed(self, i, j, player):
        # process button being pressed
        board = self.app.players_boards[player]

        # check if there are already ships on the corners (if corners exist)
        for n_i, n_j in [(i+1, j+1), (i+1, j-1), (i-1, j-1), (i-1, j+1)]:
            if 0 <= n_i < constants.BOARD_HEIGHT and 0 <= n_j < constants.BOARD_WIDTH:
                if board[n_i][n_j] != TileState.EMPTY:
                    return False  # there is a ship on any corner

        removed = []
        size = 1
        # check if there is a ship above (if above exists)
        if i > 0:  # if above exists
            if board[i-1][j] == TileState.SHIP:  # if there is a ship above
                # check if there is a ship to the sides
                if (j > 0 and board[i][j-1] == TileState.SHIP) or \
                        (j < constants.BOARD_WIDTH-1 and board[i][j+1] == TileState.SHIP):
                    return False  # there is a ship above and to the side
                # check if ship above is vertical
                if (j > 0 and board[i-1][j-1] == TileState.SHIP) or \
                        (j < constants.BOARD_WIDTH-1 and board[i-1][j+1] == TileState.SHIP):
                    return False  # ship above is vertical
                # check if there is a ship below
                if i < constants.BOARD_HEIGHT-1:  # if below exists
                    if board[i+1][j] == TileState.SHIP:
                        # check if ship below is vertical
                        if (j > 0 and board[i+1][j-1] == TileState.SHIP) or \
                                (j < constants.BOARD_WIDTH-1 and board[i+1][j+1] == TileState.SHIP):
                            return False  # ship below is vertical
                        # count how long is ship below
                        size_below = 0
                        while size_below + i < constants.BOARD_HEIGHT:
                            if board[i + size_below][j] != TileState.SHIP:
                                break
                            size_below += 1
                        size += size_below
                        removed.append(size_below)
                # count how long is ship above
                size_above = 0
                while size_above + i < constants.BOARD_HEIGHT:
                    if board[i + size_above][j] != TileState.SHIP:
                        break

                    size_below += 1




