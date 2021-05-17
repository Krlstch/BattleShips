BOARD_WIDTH = 10
BOARD_HEIGHT = 10


SHIP_COUNTS = {1: 0,
               2: 2,
               3: 0,
               4: 0}

SHIP_COUNT = sum([k*v for k, v in SHIP_COUNTS.items()])
