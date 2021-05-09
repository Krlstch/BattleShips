from src.button_grid import ButtonGrid
from src.game_states import GameState
from src import constants
from src.tile_state import TileState


class SetupScreen:
    def __init__(self, application, players_boards, button_grid, hidden=True):
        self.app = application
        self.players_boards = players_boards
        self.players_ships = [{i: 5-i for i in range(1, 5)} for _ in range(2)]

        self.setup_ui(button_grid)
        if hidden:
            self.hide()
        else:
            self.show()

    def setup_ui(self, button_grid):
        self.button_grid = button_grid
        self.button_grid.add_function(GameState.PLAYER1_PREPARING, lambda i, j: self.button_pressed(i, j, 0))
        self.button_grid.add_function(GameState.PLAYER2_PREPARING, lambda i, j: self.button_pressed(i, j, 1))

    def show(self, state=GameState.PLAYER1_PREPARING):
        self.button_grid.set_position(50, 450)
        self.button_grid.state = state
        self.button_grid.show()

    def hide(self):
        self.button_grid.hide()

    def button_pressed(self, i, j, player):
        added, removed = self.check_ship_placement(i, j, player)
        
        new_ships = self.players_ships[player].copy()
        new_ships[added] -= 1
        for ship in removed:
            new_ships[ship] += 1
        
        ssum = 0
        for k in range(4, 0, -1):
            ssum += new_ships[k]
            if ssum < 0:
                return False
        
        self.players_ships[player] = new_ships
        self.players_boards[player][i][j] = TileState.SHIP
        self.button_grid.set_button_state(i, j, TileState.SHIP)

       

    def check_ship_placement(self, i, j, player):
        # # process button being pressed
        # board = self.app.players_boards[player]

        # # check if there are already ships on the corners (if corners exist)
        # for n_i, n_j in [(i+1, j+1), (i+1, j-1), (i-1, j-1), (i-1, j+1)]:
        #     if 0 <= n_i < constants.BOARD_HEIGHT and 0 <= n_j < constants.BOARD_WIDTH:
        #         if board[n_i][n_j] != TileState.EMPTY:
        #             return False  # there is a ship on any corner

        # removed = []
        # size = 1
        # # check if there is a ship above (if above exists)
        # if i > 0:  # if above exists
        #     if board[i-1][j] == TileState.SHIP:  # if there is a ship above
        #         # check if there is a ship to the sides
        #         if (j > 0 and board[i][j-1] == TileState.SHIP) or \
        #                 (j < constants.BOARD_WIDTH-1 and board[i][j+1] == TileState.SHIP):
        #             return False  # there is a ship above and to the side
        #         # check if ship above is vertical
        #         if (j > 0 and board[i-1][j-1] == TileState.SHIP) or \
        #                 (j < constants.BOARD_WIDTH-1 and board[i-1][j+1] == TileState.SHIP):
        #             return False  # ship above is vertical
        #         # check if there is a ship below
        #         if i < constants.BOARD_HEIGHT-1:  # if below exists
        #             if board[i+1][j] == TileState.SHIP:
        #                 # check if ship below is vertical
        #                 if (j > 0 and board[i+1][j-1] == TileState.SHIP) or \
        #                         (j < constants.BOARD_WIDTH-1 and board[i+1][j+1] == TileState.SHIP):
        #                     return False  # ship below is vertical
        #                 # count how long is ship below
        #                 size_below = 0
        #                 while size_below + i < constants.BOARD_HEIGHT:
        #                     if board[i + size_below][j] != TileState.SHIP:
        #                         break
        #                     size_below += 1
        #                 size += size_below
        #                 removed.append(size_below)
        #         # count how long is ship above
        #         size_above = 0
        #         while size_above + i < constants.BOARD_HEIGHT:
        #             if board[i + size_above][j] != TileState.SHIP:
        #                 break

        #             size_below += 1


        return 1, []

