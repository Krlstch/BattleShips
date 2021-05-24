BOARD_WIDTH = 10
BOARD_HEIGHT = 10


SHIP_COUNTS = {1: 2,
               2: 1,
               3: 1,
               4: 0}

SHIP_COUNT = sum([k*v for k, v in SHIP_COUNTS.items()])

LARGEST = max(SHIP_COUNTS.keys())
SMALLEST = min(SHIP_COUNTS.keys())
