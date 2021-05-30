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

    @staticmethod
    def opposite(state):
        return {GameState.PLAYER1_PREPARING: GameState.PLAYER2_PREPARING,
                GameState.PLAYER2_PREPARING: GameState.PLAYER1_PREPARING,
                GameState.PLAYER1_PLAYING: GameState.PLAYER2_PLAYING,
                GameState.PLAYER2_PLAYING: GameState.PLAYER1_PLAYING}[state]

    @staticmethod
    def is_preparing(state):
        return state in (GameState.PLAYER1_PREPARING, GameState.PLAYER2_PREPARING)

    @staticmethod
    def is_playing(state):
        return state in (GameState.PLAYER1_PLAYING, GameState.PLAYER2_PLAYING)

    @staticmethod
    def get_player(state):
        return {GameState.PLAYER1_PREPARING: 0,
                GameState.PLAYER2_PREPARING: 1,
                GameState.PLAYER1_PLAYING: 0,
                GameState.PLAYER2_PLAYING: 1}[state]

    @staticmethod
    def get_opposite_player(state):
        return {GameState.PLAYER1_PREPARING: 1,
                GameState.PLAYER2_PREPARING: 0,
                GameState.PLAYER1_PLAYING: 1,
                GameState.PLAYER2_PLAYING: 0}[state]

    @staticmethod
    def is_same_phase(state1, state2):
        return (GameState.is_playing(state1) and GameState.is_playing(state2)) or \
            (GameState.is_preparing(state1) and GameState.is_preparing(state2))

    @staticmethod
    def next_state(state):
        return {GameState.PLAYER1_PREPARING: GameState.PLAYER2_PREPARING,
                GameState.PLAYER2_PREPARING: GameState.PLAYER1_PLAYING,
                GameState.PLAYER1_PLAYING: GameState.EMPTY_BEFORE_PLAYER2_PLAY,
                GameState.EMPTY_BEFORE_PLAYER2_PLAY: GameState.PLAYER2_PLAYING,
                GameState.PLAYER2_PLAYING: GameState.EMPTY_BEFORE_PLAYER1_PLAY,
                GameState.EMPTY_BEFORE_PLAYER1_PLAY: GameState.PLAYER1_PLAYING}[state]
