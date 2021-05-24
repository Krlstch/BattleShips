from src.special import constants


def in_bound(i, j):
    return 0 <= i < constants.BOARD_HEIGHT and \
           0 <= j < constants.BOARD_WIDTH
