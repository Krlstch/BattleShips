BOARD_WIDTH = 10
BOARD_HEIGHT = 10


SHIP_COUNTS = {1: 1,
               2: 0,
               3: 0,
               4: 0}

SHIP_COUNT = sum([k*v for k, v in SHIP_COUNTS.items()])
SHIP_TYPES_COUNT = len(SHIP_COUNTS)


LARGEST = max(SHIP_COUNTS.keys())
SMALLEST = min(SHIP_COUNTS.keys())
