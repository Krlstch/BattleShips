import enum


class TileState(enum.Enum):
    EMPTY = 0
    SHIP = 1
    EMPTY_SHOT = 2
    SHIP_SHOT = 3
