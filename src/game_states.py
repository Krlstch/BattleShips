import enum


class GameState(enum.Enum):
    START = 1
    PLAYER1_PREPARING = 2
    PLAYER2_PREPARING = 3
    EMPTY_BEFORE_PLAYER1_PLAY = 4
    PLAYER1_PLAYING = 5
    EMPTY_BEFORE_PLAYER2_PLAY = 6
    PLAYER2_PLAYING = 7
    END = 8
