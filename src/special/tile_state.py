import enum


class TileState(enum.Enum):
    EMPTY = 0
    SHIP = 1
    EMPTY_SHOT = 2
    SHIP_SHOT = 3

    @staticmethod
    def is_shot(state):
        return state in (TileState.EMPTY_SHOT, TileState.SHIP_SHOT)

    @staticmethod
    def shoot(state):
        return {TileState.EMPTY: TileState.EMPTY_SHOT,
                TileState.SHIP: TileState.SHIP_SHOT}[state]

    @staticmethod
    def opposite(state):
        return {TileState.EMPTY: TileState.SHIP,
                TileState.SHIP: TileState.EMPTY,
                TileState.EMPTY_SHOT: TileState.SHIP_SHOT,
                TileState.SHIP_SHOT: TileState.EMPTY_SHOT}[state]
